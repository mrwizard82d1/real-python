from setuptools import setup, Extension


def main():
    setup(name='fputs',
          version='1.0.0',
          description='Python interface for the fputs C library function.',
          author='Larry Jones',
          author_email='mrwizard82d1@email.com',
          ext_modules=[Extension('fputs',
                                 ['fputsmodule.c'],
                                 )],
          )


if __name__ == '__main__':
    main()
