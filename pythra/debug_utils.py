"""
PyThra Debug Utilities

This module provides a centralized way to toggle debug output on and off
throughout the PyThra framework.

Usage:
    from pythra.debug_utils import debug_print, set_debug
    
    # Enable debug output
    set_debug(True)
    
    # Print debug message (only prints if debug is enabled)
    debug_print("This is a debug message")
    
    # Disable debug output
    set_debug(False)
    
    # This won't print anything
    debug_print("This debug message is hidden")
"""

_debug_enabled = False


def set_debug(enabled: bool):
    """
    Enable or disable debug output globally.
    
    Args:
        enabled (bool): True to enable debug output, False to disable
    
    Example:
        set_debug(True)   # Turn on all debug prints
        set_debug(False)  # Turn off all debug prints
    """
    global _debug_enabled
    _debug_enabled = enabled
    if enabled:
        print("🐛 PyThra | Debug mode ENABLED")
    else:
        print("🔇 PyThra | Debug mode DISABLED")


def is_debug_enabled() -> bool:
    """
    Check if debug output is currently enabled.
    
    Returns:
        bool: True if debug is enabled, False otherwise
    """
    return _debug_enabled


def debug_print(*args, **kwargs):
    """
    Print debug output only if debug mode is enabled.
    
    This function behaves exactly like the built-in print() function,
    but only prints if debug mode is enabled via set_debug(True).
    
    Args:
        *args: Positional arguments to print (same as print())
        **kwargs: Keyword arguments (same as print())
    
    Example:
        debug_print("Value of x:", x)
        debug_print("List:", items, sep=", ")
    """
    if _debug_enabled:
        print(*args, **kwargs)


def init_debug_from_config(config):
    """
    Initialize debug mode from a PyThra config object.
    
    Args:
        config: A PyThra Config object with a .get() method
    
    Example:
        from pythra.config import Config
        config = Config('config.yaml')
        init_debug_from_config(config)
    """
    debug_enabled = config.get("Debug", False)
    set_debug(debug_enabled)
