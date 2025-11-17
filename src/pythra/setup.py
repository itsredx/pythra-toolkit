# setup.py
from setuptools import setup, find_packages
from setuptools.extension import Extension
import os

# Check if Cython is available for compilation
try:
    from Cython.Build import cythonize
    CYTHON_AVAILABLE = True
except ImportError:
    CYTHON_AVAILABLE = False
    print("WARNING: Cython not installed. Cython extensions will not be compiled.")
    print("Install Cython with: pip install Cython")

# Define Cython extensions
ext_modules = []
if CYTHON_AVAILABLE:
    ext_modules = [
        Extension(
            "pythra.reconciler_cython",
            ["pythra/reconciler_cython.pyx"],
            extra_compile_args=['-O3'],  # Optimize for speed
        ),
    ]

setup(
    name='pythra',
    version='0.1.13',
    author='Ahmad Muhammad Bashir (RED X)',
    author_email='ambashir02@gmail.com',
    description='A declarative Python UI framework for desktop apps with a webview renderer.',
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/itsredx/pythra-0.0.1', # Change this
    
    # This automatically finds your `pythra` and `pythra_cli` packages
    packages=find_packages(),
    
    # Add Cython extensions
    ext_modules=cythonize(ext_modules, language_level="3") if CYTHON_AVAILABLE else [],
    
    # This tells pip to include non-Python files found in your packages.
    # We will need to create a MANIFEST.in file to specify the template.
    include_package_data=True,

    # These are the dependencies your framework needs to run.
    install_requires=[
        'PySide6',
        'typer[all]',
        # Add any other core dependencies here
    ],
    
    # Optional: add Cython to extras for development
    extras_require={
        'dev': ['Cython>=0.29.30'],
        'fast': ['Cython>=0.29.30'],  # For fast builds with Cython
    },
    
    # --- THIS IS THE MAGIC FOR THE CLI ---
    # It creates an executable script named `pythra` that calls the `app`
    # object inside `pythra_cli.main`.
    entry_points={
        'console_scripts': [
            'pythra = pythra.pythra_cli.main:app',
        ],
    },
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
    ],
    python_requires='>=3.10',
)