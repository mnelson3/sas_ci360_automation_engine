#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import json
from pathlib import Path

from reporter import root_path
from log import Log
from connection import Connection
from security import Security
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'reporter.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Reporter:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Reporter.__mode = kwargs['mode']
		else:
			Reporter.__mode = None
		self.__mode = Reporter.__mode

		if self.__mode is not None:
			self._standard = Standard.Standard(mode=self.__mode)
			self._report_folder = self._standard.reports_path_arr
			self._secret_key = self._standard.secret_key_arr
			self._tenant_id = self._standard.tenant_id_arr
		else:
			self._standard = Standard.Standard()
			self._report_folder = self._standard.reports_path
			self._secret_key = self._standard.secret_key
			self._tenant_id = self._standard.tenant_id

		self._security = Security.Security()
		self._connection = Connection.Connection()

	@staticmethod
	def store_response(**kwargs):
		try:
			folder = kwargs['folder']
			name = kwargs['name']
			data = kwargs['data']
			json_file = Path('{0}{1}{2}{3}'.format(root_path, folder, name, '.JSON'))
			with open(json_file, 'w', encoding='utf-8') as outfile:
				json.dump(data, outfile, ensure_ascii=False, indent=4)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return


if __name__ == '__main__':
	Reporter.__init__(Reporter())
