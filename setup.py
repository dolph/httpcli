import setuptools


setuptools.setup(
    name='httpcli',
    version='1.3.0',
    description='RESTful command line HTTP client (and simpler than cURL).',
    keywords='http client cli curl rest restful',
    author='Dolph Mathews',
    author_email='dolph.mathews@gmail.com',
    url='http://github.com/dolph/httpcli',
    packages=['httpcli'],
    entry_points={'console_scripts': ['http = httpcli:main']},
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
