import platform
from PySide6.QtCore import QObject, Signal, Qt

# No need to import QApplication here; this module provides the logic, not the app instance.

# For Linux D-Bus integration
if platform.system() == "Linux":
    import dbus
    import threading
    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository import GLib

class SystemSleepManager(QObject):
    """
    Manages window states during system sleep and resume events for both Windows and Linux.
    """
    # =============================================================================
    # ADDED: Define signals for thread-safe communication
    # =============================================================================
    prepare_for_sleep = Signal()
    resuming_from_sleep = Signal()

    def __init__(self, window_manager):
        """
        Initializes the sleep manager.

        Args:
            window_manager: The instance of PyThra's WindowManager that holds all windows.
        """
        super().__init__()
        self.window_manager = window_manager
        self._window_states = {}

        # =============================================================================
        # ADDED: Connect the signals to the methods that perform GUI work
        # =============================================================================
        # When prepare_for_sleep is emitted, Qt will call minimize_all_windows on the main thread.
        self.prepare_for_sleep.connect(self.minimize_all_windows)
        # When resuming_from_sleep is emitted, Qt will call restore_all_windows on the main thread.
        self.resuming_from_sleep.connect(self.restore_all_windows)

    def setup_event_listener(self):
        """Starts the platform-specific listener for sleep/resume events."""
        if platform.system() == "Linux":
            self._start_linux_dbus_listener()
        elif platform.system() == "Windows":
            # Windows listener is handled externally by the existing WMI watcher
            # in the main webwidget module, which will call minimize/restore directly.
            print("SystemSleepManager: Windows listener will be handled by the main WMI watcher.")
            pass

    # =============================================================================
    # ADDED: New methods for the background thread to call
    # =============================================================================
    def trigger_sleep_event(self):
        """Thread-safe method to signal that the system is going to sleep."""
        self.prepare_for_sleep.emit()

    def trigger_resume_event(self):
        """Thread-safe method to signal that the system is resuming."""
        self.resuming_from_sleep.emit()
    # =============================================================================

    def _start_linux_dbus_listener(self):
        """Listens for systemd sleep signals via D-Bus in a background thread."""
        def listen_thread():
            DBusGMainLoop(set_as_default=True)
            bus = dbus.SystemBus()
            bus.add_signal_receiver(
                self._on_prepare_for_sleep,
                signal_name="PrepareForSleep",
                dbus_interface="org.freedesktop.login1.Manager"
            )
            loop = GLib.MainLoop()
            loop.run()

        # Run the D-Bus listener in a daemon thread so it doesn't block app exit
        thread = threading.Thread(target=listen_thread, daemon=True)
        thread.start()

    def _on_prepare_for_sleep(self, sleeping):
        """
        D-Bus signal handler. This runs in the background thread.
        It emits a Qt signal to safely trigger actions on the main GUI thread.
        """
        if sleeping:
            print("D-Bus: System is preparing for sleep. Emitting signal.")
            self.prepare_for_sleep.emit()
        else:
            print("D-Bus: System is resuming. Emitting signal.")
            self.resuming_from_sleep.emit()

    def minimize_all_windows(self):
        """
        Saves the state of all visible windows and then minimizes them.
        This method is now a slot and is guaranteed to run on the main GUI thread.
        """
        print("Minimizing all windows for sleep...")
        self._window_states.clear()
        # NOTE: Your original draft assumed get_all_windows(), we use the injected manager
        for window in self.window_manager.windows.values():
            if window.isVisible() and not window.isMinimized():
                self._window_states[window] = window.windowState()
                window.setWindowState(Qt.WindowMinimized)

    def restore_all_windows(self):
        """
        Restores all windows to their saved state after resuming from sleep.
        This method is now a slot and is guaranteed to run on the main GUI thread.
        """
        print("Restoring all windows after resume...")
        for window, state in self._window_states.items():
            window.setWindowState(state)
        self._window_states.clear()