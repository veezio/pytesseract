#!/usr/bin/env python

from setuptools import setup, Extension


VERSION = (0, 1, '0dev')
INCLUDE_DIRS = [
	"/usr/local/include",
]
LIBRARIES = [
	"tesseract",
	"lept",
]

tesseract_module = Extension('_tesseract',
	sources=["tesseract.i"],
	swig_opts=["-c++"] + map(lambda d: "-I" + d, INCLUDE_DIRS),
	include_dirs=map(lambda d: "-I" + d, INCLUDE_DIRS),
	libraries=LIBRARIES,
)


setup(
    name='pytesseract',
    version='.'.join([str(x) for x in VERSION]),
    description='Simple SWIG Python bindings for Tesseract',
    author='veezio',
    author_email='contact@veez.io',
    url='https://github.com/veezio/pytesseract',
	ext_modules = [tesseract_module],
	py_modules = ["tesseract"]
)
