'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on July 10, 2017

@author: jrm
'''

import sys
from setuptools import setup, find_packages, Extension

setup(
    name="enaml-native",
    version="2.9.24",
    author="frmdstryr",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url='https://github.com/frmdstryr/enaml-native/archive/master.zip',
    description="Build native mobile apps in python",
    long_description=open("README.md").read(),
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    install_requires=['enaml', 'msgpack-python'],
)