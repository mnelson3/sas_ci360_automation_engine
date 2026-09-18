#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import os
import shutil
import time

from datetime import datetime
from os import path
from pathlib import Path

from communication import root_path
from custom import UploadIdentityBridgeData, CreateIdentityBridgeReports, SendIdentityBridgeStatusMessage
from log import Log
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'listener.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Listener:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Listener.__mode = kwargs['mode']
		else:
			Listener.__mode = None
		self.__mode = Listener.__mode

		if self.__mode is not None:
			self._standard = Standard.Standard(mode=self.__mode)
			self._export_file = self._standard.export_file_arr
			self._export_change_file = self._standard.export_change_file_arr
			self._export_path = self._standard.export_path_arr
			self._export_post_path = self._standard.export_post_path_arr
		else:
			self._standard = Standard.Standard()
			self._export_file = self._standard.export_file
			self._export_change_file = self._standard.export_change_file
			self._export_path = self._standard.export_path
			self._export_post_path = self._standard.export_post_path

		self._sleep_seconds = self._standard.sleep_seconds

	def run(self):
		sleep = self._sleep_seconds

		try:
			while True:
				time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
				time_stamp_ = time_stamp.replace(':', '')
				file_chain_path = Path('{0}/{1}'.format(self._export_post_path, self._export_file))

				if path.exists(file_chain_path):
					file_export_chain = '{0}_{1}{2}'.format(self._export_file[:-4], time_stamp_, '.CSV')
					file_export_chain_path = Path('{0}{1}/{2}'.format(root_path, self._export_path, file_export_chain))
					shutil.copy(file_chain_path, file_export_chain_path)

					if path.exists(file_export_chain_path):
						os.remove(file_chain_path)

					custom_upload_data = UploadIdentityBridgeData.UploadIdentityBridgeData(mode=self.__mode)
					custom_upload_data.run(file_name=file_export_chain_path)
					time.sleep(7200)
					custom_create_reports = CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=self.__mode)
					custom_create_reports.run(time_stamp=time_stamp_)
					custom_send_status_message = SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=self.__mode)
					custom_send_status_message.run(time_stamp=time_stamp_)

				time.sleep(sleep)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None


if __name__ == '__main__':
	Listener.__init__(Listener())
