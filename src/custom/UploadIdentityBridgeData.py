#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import shutil
from datetime import datetime
from pathlib import Path

from custom import root_path
from log import Log
from connection import Connection
from reporter import Reporter
from security import Security
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'custom-upload_identity_bridge_data.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class UploadIdentityBridgeData:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			UploadIdentityBridgeData.__mode = kwargs['mode']
		else:
			UploadIdentityBridgeData.__mode = None
		self.__mode = UploadIdentityBridgeData.__mode

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

	def run(self, result=None, **kwargs):
		try:
			time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
			time_stamp_ = time_stamp.replace(':', '')

			if self.__mode is not None:
				folder = '{0}{1}/'.format(self._gDirDataResponseFileTransferLocationPost, self.__mode)
			else:
				folder = '{0}{1}/'.format(self._gDirDataResponseFileTransferLocationPost, 'development')

			export_folder = self._export_path
			external_gateway_path = self._external_gateway_path
			file_transfer_location_path = self._file_transfer_location_path

			secret_key = self._secret_key
			tenant_id = self._tenant_id
			token = self._security.generate_jwt(secret_key=secret_key, tenant_id=tenant_id)

			action = 'POST'
			data = None
			headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
			params = None
			url = 'https://{0}{1}'.format(external_gateway_path, file_transfer_location_path)
			result = self._connection.conn(action=action, data=data, headers=headers, params=params, url=url)
			self._reporter.store_response(folder=folder, name='file_transfer_location_post_{}'.format(time_stamp_), data=result)

			__signed_url = None
			if result is not None:
				__signed_url = result['signedURL']
			temporary_url = __signed_url

			if 'file_name' in kwargs:
				file_name = kwargs['file_name']
				csv_file = Path('{0}'.format(file_name))
			else:
				file_post_path = self._export_post_path
				file_export_path = Path('{0}{1}'.format(root_path, self._export_path))
				file_export = self._export_file
				file_export_timestamp = '{0}_{1}{2}'.format(file_export[:-4], time_stamp_, '.CSV')
				shutil.copy(Path('{0}/{1}'.format(file_post_path, file_export)), Path('{0}/{1}'.format(file_export_path, file_export_timestamp)))
				file_name = '{0}_{1}'.format(file_export[:-4], time_stamp_)
				csv_file = Path('{0}{1}{2}{3}'.format(root_path, export_folder, file_name, '.CSV'))

			result = None
			action = 'PUT'
			data = csv_file
			headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
			params = None
			url = temporary_url
			result = self._connection.conn(action=action, data=data, headers=headers, params=params, url=url)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return result


if __name__ == '__main__':
	UploadIdentityBridgeData.__init__(UploadIdentityBridgeData())
