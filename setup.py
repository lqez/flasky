#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages


classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='Flasky',
    version='0.1.0',
    packages=find_packages(),
    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/flasky',
    description='Lazy man\'s Flask Application',
    classifiers=classifiers,
    install_requires=[
        "Flask >= 0.9",
    ],
    test_suite='flasky.tests.flasky_test',
)
