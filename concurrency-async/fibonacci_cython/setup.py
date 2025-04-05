from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options


# These are optional
Options.docstrings = True
Options.annotate = False


# Modules to be compiled and `include_dirs` when necessary
extensions = [
    Extension(
        "fibmodule",
        ['fibmodule.py'],
    ),
]


# This is the function that is executed
setup(
    name='fibmodule', # Required

    # A list of compiler directives is available at
    # https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives

    # External function to be compiled
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3, "profile": False}),
)
