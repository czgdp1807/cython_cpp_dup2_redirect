from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    name="redirect",
    sources=["redirect.pyx"],  # Only the pyx file now
    language="c++",
    include_dirs=["."],        # Make sure .h is found
)

setup(
    name="cy_redirect_cpp",
    ext_modules=cythonize([ext]),
    zip_safe=False,
)
