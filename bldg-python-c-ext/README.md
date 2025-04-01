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

