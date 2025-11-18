"""
Cython reconciler loader and fallback mechanism.

This module attempts to import the Cython-compiled reconciler functions
and provides graceful fallback to pure Python if the extension is unavailable.
"""

# Try to import Cython-accelerated functions
try:
    from . import reconciler_cython
    print("[DEV] cython reconciler available")
    CYTHON_AVAILABLE = True
    cython_diff_props = reconciler_cython.cython_diff_props
    cython_diff_node_recursive = reconciler_cython.cython_diff_node_recursive
    cython_diff_children_recursive = reconciler_cython.cython_diff_children_recursive
except ImportError:
    print("[DEV] cython reconciler not found")
    CYTHON_AVAILABLE = False
    cython_diff_props = None
    cython_diff_node_recursive = None
    cython_diff_children_recursive = None


def get_diff_props_impl():
    """Returns the optimized _diff_props implementation."""
    if CYTHON_AVAILABLE and cython_diff_props:
        return cython_diff_props
    else:
        # Return None to signal use of Python fallback
        return None


def get_diff_node_impl():
    """Returns the optimized _diff_node_recursive implementation."""
    if CYTHON_AVAILABLE and cython_diff_node_recursive:
        return cython_diff_node_recursive
    else:
        return None


def get_diff_children_impl():
    """Returns the optimized _diff_children_recursive implementation."""
    if CYTHON_AVAILABLE and cython_diff_children_recursive:
        return cython_diff_children_recursive
    else:
        return None
