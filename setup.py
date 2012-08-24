#!/usr/bin/env python

from distutils.core import setup, Extension
from distutils.command.build import build


VERSION = (0, 1, '0dev')
INCLUDE_DIRS = [
    "/usr/include", # Debian
    "/usr/local/include", # OS X
]
LIBRARIES = [
    "tesseract",
    "lept",
]


build.sub_commands.insert(0, ('build_ext', build.has_ext_modules))


tesseract_module = Extension('_tesseract',
    sources=["tesseract.i"],
    swig_opts=["-c++"] + ["-I%s" % d for d in INCLUDE_DIRS],
    include_dirs=INCLUDE_DIRS,
    libraries=LIBRARIES,
)


setup(
    name='pytesseract',
    version='.'.join([str(x) for x in VERSION]),
    description='Simple SWIG Python bindings for Tesseract',
    author='veezio',
    author_email='contact@veez.io',
    url='https://github.com/veezio/pytesseract',
    ext_modules=[tesseract_module],
    py_modules=["tesseract"]
)
