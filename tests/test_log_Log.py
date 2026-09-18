#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from log import Log


def test_log():
	__log_file = "test.log"

	log = Log.Log.get_instance()
	log.log_file(__log_file)
	logger = log.logging()
	assert log.log_file() == "test.log"
