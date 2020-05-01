#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

import pandas

from custom import root_path
from log import Log
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'reporter.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Reporter:
	__instance = None

	@staticmethod
	def get_instance():
		if Reporter.__instance is None:
			Reporter()
		return Reporter.__instance

	def __init__(self):
		if Reporter.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			Reporter.__instance = self

		standard = Standard.Standard.get_instance()

		self._flag_test_export = standard.flag_test_export()
		self._flag_test_report = standard.flag_test_report()
		self._suppression_email_domain_list = standard.suppression_email_domain_list()
		self._suppression_form_name_list = standard.suppression_form_name_list()

	@staticmethod
	def build_report(**kwargs):
		try:
			prefix = kwargs['prefix']
			name = kwargs['name']
			json_response = kwargs['json_response']

			report_file = Path(root_path + Standard.gDirReport + prefix + name + '.csv')

			dataframe = pandas.read_csv(filepath_or_buffer=json_response, sep=',', delimiter=',', encoding='UTF-8')

			dataframe.to_csv(path_or_buf=report_file, sep=',', index=False, header=False)
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None
		finally:
			return


if __name__ == '__main__':
	Reporter.__init__(Reporter())
