#!/bin/env python3
from setuptools import setup, find_packages

setup(
    name='simplepos',
    version='0.1',
    packages=find_packages(exclude=['test', 'test.*']),
    url='https://github.com/axmachado/simplepos',
    license='GPLv3',
    author='Alexandre Machado',
    author_email='axmachado@gmail.com',
    description='SimplePOS language compiler to POSXML ',
    scripts = [ 'spl', 'spc'],
    install_requires=['antlr4-python3-runtime']
)
