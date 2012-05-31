#!/usr/bin/env python

from setuptools import setup

README = 'README.rst'
with open(README) as file:
    long_description = file.read()

setup(
        name='httpcli',
        version='1.1.2',
        description='RESTful command line HTTP client '
            '(and simpler than cURL).',
        long_description=long_description,
        keywords='http client cli curl rest restful',
        author='Dolph Mathews',
        author_email='dolph.mathews@gmail.com',
        url='http://github.com/dolph/httpcli',
        packages=['httpcli'],
        scripts=['bin/http'],
        package_data = {'': [README]},
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
