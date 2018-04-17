#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
import birb
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'birb'
DESCRIPTION = 'Send tweets from your CLI'
URL = 'https://github.com/ovelny/birb'
EMAIL = 'this.is.ovelny@gmail.com'
AUTHOR = 'Ovelny'
REQUIRES_PYTHON = '>=3'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'twitterAPI', 'click'
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Ask for twitter API keys
print("Create an app on https://apps.twitter.com and paste the following infos to use it: ")
consumer_key = input("Paste consumer key here: ")
consumer_secret = input("Paste consumer secret here: ")
access_token_key = input("Paste access token here: ")
access_token_secret = input("Paste access token secret here: ")

credentials = ('api = TwitterAPI(' + '\'' + consumer_key + '\'' + ','
                                   + '\'' + consumer_secret + '\'' + ','
                                   + '\'' + access_token_key + '\'' + ','
                                   + '\'' + access_token_secret + '\'' + ')\n')

with open(os.path.join(here, 'birb.py'), 'r+', encoding='utf-8') as script:
    content = script.readlines()
    script.seek(0)
    for line in content:
        if "api =" not in line:
            script.write(line)
        else:
            script.write(credentials)
    script.truncate()

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['birb'],
     entry_points={
         'console_scripts': ['birb=birb:birb'],
     },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3'
    ]
)