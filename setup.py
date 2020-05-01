#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from setuptools import setup

setup(
    name='automation',
    version='1.0.0',
    packages=['communication', 'connection', 'custom', 'log', 'main', 'reporter', 'scheduler', 'security', 'standard'],
    package_dir={'': 'src'},
    namespace_packages=['SAS_CI360_'],
    url='www.sas.com',
    license='SAS Institute Inc.',
    author='manels',
    author_email='Mark.Nelson@sas.com',
    description=''
)
