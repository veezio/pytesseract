#!/usr/bin/env python

import os
from distutils.core import setup, Extension
from distutils.command.build import build


VERSION = (0, 1, '0dev')
INCLUDE_DIRS = [
    "/usr/include", # Debian
    "/usr/local/include", # OS X
]
TESSERACT_OPT_INCLUDES = [
    "pageiterator.h",
    "resultiterator.h",
    "ltrresultiterator.h",
]
LIBRARIES = [
    "tesseract",
    "lept",
]
COMPLETE_BINDING = "tesseract.complete.i"


def resolve_optional_includes():
    binding = open("tesseract.i").read()
    files = set()
    for d in INCLUDE_DIRS:
        for include_file in TESSERACT_OPT_INCLUDES:
            if os.path.exists(os.path.join(d, "tesseract", include_file)):
                files.add(include_file)
    binding += "\n%s\n" % "\n".join(["%%include <tesseract/%s>" % f for f in files])
    with open(COMPLETE_BINDING, "w") as fp:
        fp.write(binding)
resolve_optional_includes()


tesseract_module = Extension('_tesseract',
    sources=[COMPLETE_BINDING],
    swig_opts=["-c++"] + ["-I%s" % d for d in INCLUDE_DIRS],
    include_dirs=INCLUDE_DIRS,
    libraries=LIBRARIES,
)


build.sub_commands.insert(0, ('build_ext', build.has_ext_modules))
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

os.unlink(COMPLETE_BINDING)