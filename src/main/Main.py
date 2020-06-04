#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from multiprocessing import Process
from pathlib import Path

from main import root_path
from log import Log
from listener import Listener
from scheduler import Scheduler
from standard import Standard


__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'main.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


def start():
	try:
		standard = Standard.Standard()
		modes = standard.mode_name_arr

		for item in modes:
			p = Process(target=run_scheduler_chain, args=(item,))
			p.start()

			p = Process(target=run_scheduler_change, args=(item,))
			p.start()

			p = Process(target=run_listener, args=(item,))
			p.start()
	except Exception as e:
		logger.exception('Exception occurred: {}'.format(str(e)))
		return None
	finally:
		return


def run_listener(mode):
	try:
		listener = Listener.Listener(mode=mode)
		return listener.run()
	except Exception as e:
		logger.exception('Exception occurred: {}'.format(str(e)))
		return None


def run_scheduler_chain(mode):
	try:
		scheduler = Scheduler.Scheduler(mode=mode)
		return scheduler.chain_run()
	except Exception as e:
		logger.exception('Exception occurred: {}'.format(str(e)))
		return None


def run_scheduler_change(mode):
	try:
		scheduler = Scheduler.Scheduler(mode=mode)
		return scheduler.change_run()
	except Exception as e:
		logger.exception('Exception occurred: {}'.format(str(e)))
		return None


if __name__ == '__main__':
	start()
