#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from datetime import datetime
import json
from pathlib import Path

from custom import root_path
from log import Log
from connection import Connection
from reporter import Reporter
from security import Security
from standard import Standard


__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'custom-tables_action.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class TableActions:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			TableActions.__mode = kwargs['mode']
		else:
			TableActions.__mode = None
		self.__mode = TableActions.__mode

		if self.__mode is not None:
			self._reporter = Reporter.Reporter(mode=self.__mode)
			self._standard = Standard.Standard(mode=self.__mode)
			self._export_file = self._standard.export_file_arr
			self._export_path = self._standard.export_path_arr
			self._export_post_path = self._standard.export_post_path_arr
			self._external_gateway_path = self._standard.external_gateway_path_arr
			self._secret_key = self._standard.secret_key_arr
			self._tenant_id = self._standard.tenant_id_arr
		else:
			self._reporter = Reporter.Reporter()
			self._standard = Standard.Standard()
			self._export_file = self._standard.export_file
			self._export_path = self._standard.export_path
			self._export_post_path = self._standard.export_post_path
			self._external_gateway_path = self._standard.external_gateway_path
			self._secret_key = self._standard.secret_key
			self._tenant_id = self._standard.tenant_id

		self._connection = Connection.Connection()
		self._security = Security.Security()
		self._gDirDataResponseFileTransferLocationPost = self._standard.gDirDataResponseFileTransferLocationPost
		self._file_transfer_location_path = self._standard.file_transfer_location_path

	def tables_get(self):
		time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
		time_stamp_ = time_stamp.replace(':', '')

		folder = self._standard.gDirDataResponseTablesGet

		secret_key = self._secret_key
		tenant_id = self._tenant_id
		token = self._security.generate_jwt(secret_key=secret_key, tenant_id=tenant_id)

		action = 'GET'
		data = None
		headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
		params = None
		url = 'https://{0}'.format(self._standard.tables_path)
		result = self._connection.conn(action=action, data=data, headers=headers, params=params, url=url)
		self._reporter.store_response(folder=folder, name='table_get_{}'.format(time_stamp_), data=result)

	def tables_by_id_get(self, **kwargs):
		time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
		time_stamp_ = time_stamp.replace(':', '')

		folder = self._standard.gDirDataResponseTablesGet

		secret_key = self._secret_key
		tenant_id = self._tenant_id
		token = self._security.generate_jwt(secret_key=secret_key, tenant_id=tenant_id)

		if 'table_id' in kwargs:
			table_id = kwargs['table_id']
		else:
		# table_id = __standard.identity_bridge_table_id
		# assert table_id == __standard.identity_bridge_table_id

		file_name = 'table_get_{}'.format(time_stamp)
		json_file = Path('{0}{1}{2}{3}'.format(root_path, self._standard.gDirDataResponseTablesGet, file_name, '.JSON'))

		print('json_file : {}'.format(json_file))
		with open(json_file, 'r', encoding='utf-8') as outfile:
			result = json.load(outfile)
			__url = None
			if result is not None:
				for item in result['items']:
					if item['id'] == table_id:
						for i in item['links']:
							if i['method'] == 'GET':
								__url = i['href']
								print('__url : {0}'.format(__url))
			temporary_url = __url
			assert temporary_url is not None and temporary_url == __url

		action = 'GET'
		assert action == 'GET'
		data = None
		assert data is None
		headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
		assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'}
		params = None
		assert params is None
		url = temporary_url
		assert url == 'https://{0}/{1}'.format(__standard.tables_path(), table_id)
		result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
		assert result is not None
		folder = __standard.gDirDataResponseTablesGet
		__reporter.store_response(folder=folder, name='{}'.format(table_id), data=result)


if __name__ == '__main__':
	TableActions.__init__(TableActions())
