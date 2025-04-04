#include <stdio.h>

#include <Python.h>

int fib(const int n) {
    return n == 0 ? 0 : (n == 1 ? 1 : fib(n - 2) + fib(n - 1));
}

static PyObject* fibmodule_fib(PyObject* self, PyObject* args) {
    int n;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    int result = -1;
    Py_BEGIN_ALLOW_THREADS
    result = fib(n);
    Py_END_ALLOW_THREADS

    return PyLong_FromLong(result);
}

static PyMethodDef fibmethods[] = {
    {"fib", fibmodule_fib, METH_VARARGS, "Calculate the nth Fibonacci"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibmodule = {
    PyModuleDef_HEAD_INIT,
    "fibmodule",
    "Efficient Fibonacci number calculator",
    -1,
    fibmethods
};

PyMODINIT_FUNC PyInit_fibmodule(void) {
    return PyModule_Create(&fibmodule);
}
