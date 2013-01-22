#!/usr/bin/env python

__author__ = 'Jason Corbett'

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="slickqa-narc",
    description="A program responsible for responding to Slick events",
    version="2.0" + open("build.txt").read(),
    license="License :: OSI Approved :: Apache Software License",
    long_description=open('README.txt').read(),
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rst', '*.html']},
    include_package_data=True,
    install_requires=['slickqa>=2.0.8', 'kombu>=2.5.4'],
    author="Slick Developers",
    url="http://code.google.com/p/slickqa"
)
