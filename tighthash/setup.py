from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['ctighthash.pyx']

extensions = [Extension("ctighthash", sourcefiles, extra_compile_args=['-std=c99'])]

setup(
   ext_modules = cythonize(extensions)
) 
