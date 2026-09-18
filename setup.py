#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from setuptools import setup

setup(
    name='sas_ci360_automation_engine',
    version='1.0.0',
    packages=['communication', 'connection', 'custom', 'log', 'main', 'reporter', 'scheduler', 'security', 'standard'],
    package_dir={'': 'src'},
    url='https://github.com/mnelson3/sas_ci360_automation_engine',
    license='Apache-2.0',
    author='Mark Nelson',
    author_email='support@nelsongrey.com',
    description='Automation engine that downloads Discover data from the SAS Customer Intelligence 360 '
                 'datahub, applies business rules to it, and uploads the resulting CSV file back to CI360.'
)
