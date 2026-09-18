#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from unittest.mock import patch

from scheduler import Scheduler

# chain_run()/change_run() schedule a job and then loop forever
# (while True: run_pending(); time.sleep(...)), by design, for the live
# service. That loop is only reachable in a test by mocking time.sleep to
# break out of it; calling these methods unmocked hangs indefinitely and
# defeats pytest-timeout, since the loop's own `except Exception` swallows
# the timeout signal along with everything else.
_STOP_LOOP = RuntimeError("stop scheduler loop for test")


def test_run_mode():
	mode = 'development'
	scheduler = Scheduler.Scheduler(mode=mode)
	with patch('scheduler.Scheduler.time.sleep', side_effect=_STOP_LOOP):
		scheduler.chain_run()
		scheduler.change_run()


def test_run():
	scheduler = Scheduler.Scheduler()
	with patch('scheduler.Scheduler.time.sleep', side_effect=_STOP_LOOP):
		scheduler.chain_run()
		scheduler.change_run()
