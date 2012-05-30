#!/usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name='HTTP CLI Client',
        version='1.0',
        description='Command line HTTP cLient, similar to cURL.',
        long_description=read('README'),
        keywords='http client cli curl rest restful',
        author='Dolph Mathews',
        author_email='dolph.mathews@gmail.com',
        url='http://dolphmathews.com/',
        packages=['http'],
        scripts=['bin/http'],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
        ],
)
