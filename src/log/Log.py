#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import logging


class Log:
	__instance = None

	@staticmethod
	def get_instance():
		if Log.__instance is None:
			Log()
		return Log.__instance

	def __init__(self, **kwargs):
		if Log.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			Log.__instance = self

			if 'log_file' in kwargs:
				self._log_file = kwargs['log_file']

	def log_file(self, value=None):
		if value:
			self._log_file = value
		try:
			return self._log_file
		except AttributeError or Exception as e:
			logging.exception('Exception occurred: {}'.format(str(e)))
			return None

	def logging(self):
		logger = logging.getLogger()
		formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
		handler = logging.FileHandler(self.log_file())
		handler.setFormatter(formatter)
		logger.setLevel(logging.ERROR)
		logger.addHandler(handler)
		return logger


if __name__ == '__main__':
	Log.__init__(Log())
