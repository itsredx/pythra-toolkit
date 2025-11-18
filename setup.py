# setup.py
from setuptools import setup, Extension
import os

# Check if Cython is available
try:
    from Cython.Build import cythonize
    CYTHON_AVAILABLE = True
except ImportError:
    CYTHON_AVAILABLE = False
    print("WARNING: Cython not installed. Cython extensions will not be compiled.")

# 1. Correct Source Path: 
#    Your file is at src/pythra/pythra/reconciler_cython.pyx
source_file = "src/pythra/pythra/reconciler_cython.pyx"

# 2. Correct Extension Name:
#    Since the file is inside the 'pythra' subpackage, the module name
#    should be 'pythra.pythra.reconciler_cython' so relative imports work.
extension_name = "pythra.pythra.reconciler_cython"

ext_modules = []
if CYTHON_AVAILABLE and os.path.exists(source_file):
    ext_modules = [
        Extension(
            name=extension_name,
            sources=[source_file],
            extra_compile_args=['-O3'] if os.name != 'nt' else ['/Ox'], # /Ox is O3 for MSVC (Windows)
        ),
    ]
elif CYTHON_AVAILABLE and not os.path.exists(source_file):
    print(f"❌ Error: Could not find source file at {source_file}")

setup(
    ext_modules=cythonize(ext_modules, language_level="3") if ext_modules else [],
)