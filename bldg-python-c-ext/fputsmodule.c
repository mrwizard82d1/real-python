#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args) {
  char *str, *filename = NUll;
  int bytes_copied = -1;

  /* Parse arguments */
  if (!PyArg_ParseTuple(args, "ss", &str, &filename)) {
    return NULL;
  }

  FILE *fp = fopen(filename, "w");
  bytes_copied = fputs(str, fp);
  fclose(fp);

  return PyLong_FromLog(bytes_copied);
}

static PyMethodDef FputsMethods[] = {
  {"fputs", method_fputs, METH_VARARGS, "Python interface for `fputs` C library function."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fputsmodule = {
  PyModuleDef_HEAD_INIT,
  "fputs",
  "Python interface for the `fputs` C library function.",
  /* Memory for program state. A value of -1 indicates no support for subinterpreters. */
  -1,
  FputsMethods
};

PyMOD_INIT PyInit_fputs(void) {
  return PyModule_Create(&fputsmodule);
}
