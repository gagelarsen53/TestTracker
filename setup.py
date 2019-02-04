"""
********************************************************************************
* Name: setup.py
* Author: Gage Larsen
* Created On: February 4th, 2019
* Copyright: (c) GLD
* License: BSD 2-Clause
********************************************************************************
"""
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = []

version = '1.0.0'

setup(
    name='Tracker',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='BSD 2-Clause License',
    description='Test Tracker Django Site Project',
    long_description=README,
    author='Gage Larsen',
    author_email='gagelarsen53@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=requires,
    extras_require={
        'tests': [
            'requests_mock',
        ],
    },
)