#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import time

from schedule import run_pending, every
from pathlib import Path

from log import Log
from main import Main
from scheduler import root_path
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'scheduler.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Scheduler:
	__instance = None

	@staticmethod
	def get_instance():
		if Scheduler.__instance is None:
			Scheduler()
		return Scheduler.__instance

	def __init__(self):
		if Scheduler.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			Scheduler.__instance = self

		standard = Standard.Standard.get_instance()

		self._interval = standard.interval()

	@staticmethod
	def job():
		try:
			j = Main.Main.get_instance()
			j.run()
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def run(self):
		try:
			self.job()
			i = self._interval
			every(i).hour.at(':00').do(self.job)
			while True:
				run_pending()
				time.sleep(60)
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None


if __name__ == '__main__':
	Scheduler.__init__(Scheduler())
