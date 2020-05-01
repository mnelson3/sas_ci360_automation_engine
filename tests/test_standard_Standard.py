#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import datetime

from standard import Standard


def test_get_date_time_stamp():
	t = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	print(t)
	standard = Standard.Standard.get_instance()
	print(standard)
	assert standard.get_date_time_stamp() == t
