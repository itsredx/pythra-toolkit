# pythra/__init__.py

"""
PyThra Framework Initialization

This package provides a Flutter-inspired UI framework for desktop applications
using Python, rendering via HTML/CSS/JS in a webview (like PySide6 QtWebEngine).
"""

# --- Core Framework Classes ---
from .core import Framework
from .config import Config  # Expose configuration access

# --- Base Widget and State Management ---
from .base import Widget

# Assuming Key class is defined in base.py or reconciler.py
# If in reconciler.py, change the import below:
# from .reconciler import Key
from .base import Key  # Prefer placing Key in base.py as it's fundamental
from .state import State, StatefulWidget, StatelessWidget
from .icons import Icons, IconData
from .controllers import (
    TextEditingController,
    SliderController,
    VirtualListController,
    DropdownController,
)
from .events import TapDetails, PanUpdateDetails
from .drived_widgets.dropdown.dropdown import DerivedDropdown
from .drived_widgets.dropdown.controller import DerivedDropdownController
from .drived_widgets.dropdown.style import DerivedDropdownTheme
from .navigation import Navigator, NavigatorState, PageRoute


# --- Styling Utilities and Constants ---
# Import common styling classes and enums/constants
from .styles import (
    EdgeInsets,
    Alignment,
    TextAlign,
    BoxConstraints,
    Colors,
    Offset,
    BoxShadow,
    ClipBehavior,
    ImageFit,
    MainAxisSize,
    Axis,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextStyle,
    BorderStyle,
    BorderRadius,
    BorderSide,
    ButtonStyle,
    ScrollPhysics,
    Overflow,
    StackFit,
    TextDirection,
    TextBaseline,
    VerticalDirection,
    BoxFit,
    BoxDecoration,
    BoxDecoration,
    InputDecoration,
    ScrollbarTheme,
    SliderTheme,
    CheckboxTheme,
    SwitchTheme,
    RadioTheme,
    DropdownTheme,
    GradientBorderTheme,
    GradientTheme,
)

from .drawing import (
    PathCommandWidget,
    MoveTo,
    LineTo,
    ClosePath,
    ArcTo,
    QuadraticCurveTo,
    create_rounded_polygon_path,
    RoundedPolygon,
    PolygonClipper,
)

# --- Widget Implementations ---
# Expose common widgets directly. Users can import less common ones
# specifically from framework.widgets if needed.
from .widgets import (
    Container,
    Text,
    TextButton,
    ElevatedButton,
    IconButton,
    FloatingActionButton,
    SingleChildScrollView,
    GlobalScrollbarStyle,
    Scrollbar,
    Column,
    Row,
    AssetImage,
    AssetIcon,
    NetworkImage,
    Image,
    Icon,
    # _VirtualListViewState,
    VirtualListView,
    ListView,
    GridView,
    Stack,
    Positioned,
    Expanded,
    Spacer,
    SizedBox,
    AppBar,
    BottomNavigationBarItem,
    BottomNavigationBar,
    # MyMainScreen,
    # _MyMainScreenState,
    Scaffold,
    TextField,
    Divider,
    Drawer,
    EndDrawer,
    BottomSheet,
    SnackBarAction,
    SnackBar,
    Center,
    Placeholder,
    Padding,
    Align,
    AspectRatio,
    FittedBox,
    FractionallySizedBox,
    Flex,
    Wrap,
    Dialog,
    # MyScreenState,
    ClipPath,
    ListTile,
    Slider,
    # _MySettingsPageState,
    Checkbox,
    Switch,
    Radio,
    # MyFormState,
    Dropdown,
    # MyFormState,
    GestureDetector,
    # DraggableBoxState,
    GradientBorderContainer,
    GradientClipPathBorder,
    # Add any other core widgets you want easily accessible...
)

# --- Define __all__ for explicit export control ---
# This list controls what `from framework import *` imports,
# and also serves as documentation for the public API.
__all__ = [
    # --- Core & Base ---
    "Framework",
    "Config",
    "Widget",
    "Key",
    "State",
    "StatefulWidget",
    "StatelessWidget",
    # --- Styling ---
    "EdgeInsets",
    "Alignment",
    "TextAlign",
    "BoxConstraints",
    "Colors",
    "Offset",
    "BoxShadow",
    "ClipBehavior",
    "ImageFit",
    "MainAxisSize",
    "Axis",
    "MainAxisAlignment",
    "CrossAxisAlignment",
    "TextStyle",
    "BorderStyle",
    "BorderRadius",
    "BorderSide",
    "ButtonStyle",
    "ScrollPhysics",
    "Overflow",
    "StackFit",
    "TextDirection",
    "TextBaseline",
    "VerticalDirection",
    "BoxFit",
    "BoxDecoration",
    "BoxDecoration",
    "InputDecoration",
    "ScrollbarTheme",
    "SliderTheme",
    "CheckboxTheme",
    "SwitchTheme",
    "RadioTheme",
    "DropdownTheme",
    "GradientBorderTheme",
    "GradientTheme",
    # --- Widgets ---
    "Container",
    "Text",
    "TextButton",
    "ElevatedButton",
    "IconButton",
    "FloatingActionButton",
    "SingleChildScrollView",
    "GlobalScrollbarStyle",
    "Scrollbar",
    "Column",
    "Row",
    "AssetImage",
    "AssetIcon",
    "NetworkImage",
    "Image",
    "Icon",
    "Icons",
    "IconData",
    # '_VirtualListViewState',
    "VirtualListView",
    "ListView",
    "GridView",
    "Stack",
    "Positioned",
    "Expanded",
    "Spacer",
    "SizedBox",
    "AppBar",
    "BottomNavigationBarItem",
    "BottomNavigationBar",
    # 'MyMainScreen',
    # '_MyMainScreenState',
    "Scaffold",
    "TextField",
    "Divider",
    "Drawer",
    "EndDrawer",
    "BottomSheet",
    "SnackBarAction",
    "SnackBar",
    "Center",
    "Placeholder",
    "Padding",
    "Align",
    "AspectRatio",
    "FittedBox",
    "FractionallySizedBox",
    "Flex",
    "Wrap",
    "Dialog",
    # 'MyScreenState',
    "ClipPath",
    "ListTile",
    "Slider",
    # '_MySettingsPageState',
    "Checkbox",
    "Switch",
    "Radio",
    # 'MyFormState',
    "Dropdown",
    # 'MyFormState',
    "GestureDetector",
    # 'DraggableBoxState',
    "GradientBorderContainer",
    "GradientClipPathBorder",
    # --- Derived ---
    "DerivedDropdown",
    "DerivedDropdownTheme",
    "Navigator",
    "NavigatorState",
    "PageRoute",
    # --- Controllers ---
    "TextEditingController",
    "SliderController",
    "VirtualListController",
    "DropdownController",
    "DerivedDropdownController",
    "TapDetails",
    "PanUpdateDetails",
]


# --- Package Version (Optional) ---
__version__ = "0.1.10"  # Example version

print("PyThra Toolkit Initialized")  # Optional: Confirmation message
