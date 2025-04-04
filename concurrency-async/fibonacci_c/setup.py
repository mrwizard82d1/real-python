from setuptools import setup, Extension


setup(
    name='fibmodule',
    version='1.0.0',
    ext_modules=[Extension('fibmodule', ['fibmodule.c'])],
)
