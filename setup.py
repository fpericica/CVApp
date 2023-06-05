# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='CVApp',
    version='1.0.0',
    description='Sample CV App for retrieving data',
    long_description=readme,
    author='Felix C. Pericică',
    author_email='pericicafelixcristian@gmail.com',
    url='',
    packages=find_packages(exclude=('tests'))
)
