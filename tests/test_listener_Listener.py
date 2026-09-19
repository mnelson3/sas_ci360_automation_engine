#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from unittest.mock import patch

from listener import Listener

# run() loops forever (while True: ...; time.sleep(sleep)) by design, for
# the live service. That loop is only reachable in a test by mocking
# time.sleep to break out of it; calling it unmocked hangs indefinitely
# and defeats pytest-timeout, since the loop's own `except Exception`
# swallows the timeout signal along with everything else (see
# test_scheduler_Scheduler.py for the same pattern).
_STOP_LOOP = RuntimeError("stop listener loop for test")


def test_listener_run():
	listener = Listener.Listener()
	with patch('listener.Listener.time.sleep', side_effect=_STOP_LOOP):
		listener.run()
