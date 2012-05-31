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
        name='httpcli',
        version='1.1',
        description='RESTful command line HTTP client '
            '(and simpler than cURL).',
        long_description=read('README.rst'),
        keywords='http client cli curl rest restful',
        author='Dolph Mathews',
        author_email='dolph.mathews@gmail.com',
        url='http://github.com/dolph/httpcli',
        packages=['httpcli'],
        scripts=['bin/http'],
        install_requires=[
            'argparse',
            'httplib2',
            'setuptools',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Utilities',
        ],
)
