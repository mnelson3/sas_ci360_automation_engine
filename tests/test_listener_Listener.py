#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import time
from os import path
from listener import Listener


def test_listener_run():
	assert path.exists('D:\Clients\Example_Financial\SAS360\CHAINING\DEVELOPMENT\SASCHAIN.CSV')
	assert path.exists('D:\Clients\Example_Financial\SAS360\CHAINING\DEVELOPMENT\SASCHANGE.CSV')

	listener = Listener.Listener()
	listener.run()
	time.sleep(15)

	assert not path.exists('D:\Clients\Example_Financial\SAS360\CHAINING\DEVELOPMENT\SASCHAIN.CSV')
	assert not path.exists('D:\Clients\Example_Financial\SAS360\CHAINING\DEVELOPMENT\SASCHANGE.CSV')
