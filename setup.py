from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    name="redirect",
    sources=["redirect.pyx", "redirect_cpp.cpp"],
    language="c++",
)

setup(
    name="cy_redirect_cpp",
    ext_modules=cythonize([ext]),
    zip_safe=False,
)
