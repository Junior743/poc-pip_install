#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

try:
    long_description = open("README.rst", "U").read()
except IOError:
    long_description = "See https://github.com/Junior743/poc-pip_install"

import libpip2pi
version = "%s.%s.%s" %libpip2pi.__version__

setup(
    name="poc-pip_install",
    version=version,
    url="https://github.com/Junior743/poc-pip_install",
    author="Junior",
    author_email="carlos.junior@tevec.com.br",
    description="""
        pip2pi builds a PyPI-compatible package repository from pip
        requirements
    """,
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dir2pi = libpip2pi.commands:dir2pi',
            'pip2pi = libpip2pi.commands:pip2pi',
            'pip2tgz = libpip2pi.commands:pip2tgz',
            'pip2whl = libpip2pi.commands:pip2whl',
        ],
    },
    install_requires=[
        "pip>=1.1",
    ],
    license="BSD",
    classifiers=[ x.strip() for x in """
        Development Status :: 4 - Beta
        Environment :: Console
        Intended Audience :: Developers
        Intended Audience :: System Administrators
        License :: OSI Approved :: BSD License
        Natural Language :: English
        Operating System :: OS Independent
        Programming Language :: Python
        Topic :: Software Development
        Topic :: Utilities
    """.split("\n") if x.strip() ],
)
