Code from the Real Python tutorial, "Building a Python C Extension Module."

https://realpython.com/build-python-c-extension-module/

** How to build extension on a Mac M1

After writing the code, execute the following scripts in order 
in the project virtual environment

1. source ./set_archflags.sh
2. ./build_ext.sh
3. ./install_ext.sh
4. ./verify_ext_build.sh

Test the extension by opening the Python interpreter and executing `import fputs`

*** Additional note

Apparently, I did another step before building. If I

- Restart PyCharm
- Open a new terminal within PyCharm
- Run the previous steps

The build fails when executing ./build.ext.sh because of the presence of "extra" files:

- basic-fputs.c
- test_fputs.py

To work around this, I must

- "Delete" these two files (for example, by renaming them to <filename>.hide)
- Perform the steps listed previously to build the extension
- "Undelete" these two files

I can then open a Python interpreter and import the `fputs` module.

I thought I had the process down; I'm less certain now.