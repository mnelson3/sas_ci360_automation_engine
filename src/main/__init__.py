#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import os
import sys

current_file = __file__
real_path = os.path.realpath(current_file)
dir_path = os.path.dirname(real_path)
src_path = os.path.abspath(os.path.join(dir_path, os.pardir))
root_path = os.path.abspath(os.path.join(src_path, os.pardir))
sys.path.append(dir_path)
