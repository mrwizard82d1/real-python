To write a Python extension in CLion, follow these steps: 

• Install Python and CLion: Ensure Python is installed and its path is added to the system environment variables. Install CLion, a cross-platform IDE for C and C++. 
• Create a new project: In CLion, create a new project, selecting "C Executable" as the project type. CLion relies on CMake for project management, even for Python projects. 
• Configure Python interpreter: Go to File | Settings | Build, Execution, Deployment | Python Interpreter. Add or select a Python interpreter. CLion's CMake integration will pick up this interpreter and related environment variables. 
• Write the C/C++ extension code: Create a new .c or .cpp file for your extension. Use the Python C API to define the module and its functions. All symbols in extension modules should be declared static, except for the module's initialization function. Symbols that should be accessible from other extension modules must be exported in a different way. [1]  

    #include <Python.h>

    static PyObject* example_function(PyObject* self, PyObject* args) {
        // Function implementation
        return Py_BuildValue("i", 42);
    }

    static PyMethodDef ExampleMethods[] = {
        {"example_function", example_function, METH_NOARGS, "An example function."},
        {NULL, NULL, 0, NULL} // Sentinel
    };

    static struct PyModuleDef examplemodule = {
        PyModuleDef_HEAD_INIT,
        "example",   // name of module
        NULL, // module documentation, may be NULL
        -1,       // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
        ExampleMethods
    };

    PyMODINIT_FUNC PyInit_example(void) {
        return PyModule_Create(&examplemodule);
    }

• Create setup.py: Create a setup.py file to build the extension. 

    from setuptools import setup, Extension

    setup(
        name='example',
        version='1.0',
        ext_modules=[Extension('example', ['example.c'])]
    )

• Configure CMake: Modify the CMakeLists.txt file to include the setup.py build process. 

    cmake_minimum_required(VERSION 3.10)
    project(my_python_extension)

    find_package(Python REQUIRED)

    add_custom_target(
        build_extension
        COMMAND ${PYTHON_EXECUTABLE} setup.py build_ext --inplace
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/example.c ${CMAKE_CURRENT_SOURCE_DIR}/setup.py
    )

• Build the extension: Build the build_extension target in CLion. This will compile the C/C++ code and create the extension module. 
• Run and debug: Create a Python script to import and use the extension. Configure a Python run configuration in CLion to run the script. To debug the extension, you might need to configure a "Custom Build Application" run configuration with the Python interpreter as the executable and then debug it. 

import example

print(example.example_function())

Generative AI is experimental.

[1] https://docs.python.org/3/extending/extending.html

Retrieved from Google using search terms, 
"using clion to write a python extension" on 04-Apr-2025.

I originally used a different sequence of search terms that included 
different build steps. I believe the two build steps were:

- `python setup.py build_ext --inplace`
- `python seup.py install`

To test this function, try the following steps:

- `uv run ipython` (or `uv run python`)

Afterward, the test Python session should produce the following results

```
>>> import fibmodule
>>> fibmodule.__doc__
'Efficient Fibonacci number calculator'
>>> dir(fibmodule)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib']
>>> fibmodule.fib.__doc__
'Calculate the nth Fibonacci'
>>> fibmodule.fib(0)
0
>>> fibmodule.fib(1)
1
>>> fibmodule.fib(2)
1
>>> fibmodule.fib(3)
2
>>> fibmodule.fib(4)
3
>>> fibmodule.fib(5)
5
>>> fibmodule.fib(6)
8
>>> fibmodule.fib(35)
9227465
```
