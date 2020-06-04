#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import time
from pathlib import Path

from schedule import run_pending, every

from custom import SendIdentityBridgeSupportMessage, UploadIdentityBridgeData
from log import Log
from scheduler import root_path
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'scheduler.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Scheduler:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Scheduler.__mode = kwargs['mode']
		else:
			Scheduler.__mode = None
		self.__mode = Scheduler.__mode

		if self.__mode is not None:
			self._custom_send_support_message = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=self.__mode)
			self._custom_upload_data = UploadIdentityBridgeData.UploadIdentityBridgeData(mode=self.__mode)
			self._standard = Standard.Standard(mode=self.__mode)
		else:
			self._custom_send_support_message = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage()
			self._custom_upload_data = UploadIdentityBridgeData.UploadIdentityBridgeData()
			self._standard = Standard.Standard()

		self._schedule_job_chain = self._standard.schedule_job_chain
		self._schedule_job_change = self._standard.schedule_job_change
		self._sleep_seconds = self._standard.sleep_seconds

	def chain_run(self):
		try:
			sleep_seconds = self._sleep_seconds
			schedule_job_chain = self._schedule_job_chain
			# job_ = schedule_job_chain[0]
			day_ = str(schedule_job_chain[1]).lower()
			hour_ = schedule_job_chain[2]
			minute_ = schedule_job_chain[3]
			time_ = '{0}:{1}'.format(hour_, minute_)

			if day_ == 'monday':
				every().monday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'tuesday':
				every().tuesday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'wednesday':
				every().wednesday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'thursday':
				every().thursday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'friday':
				every().friday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'saturday':
				every().saturday.at(time_).do(job_func=self.chain_job)
			elif day_ == 'sunday':
				every().sunday.at(time_).do(job_func=self.chain_job)
			else:
				every().day.at(time_).do(job_func=self.chain_job)

			while True:
				run_pending()
				time.sleep(sleep_seconds)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	def change_run(self):
		try:
			sleep_seconds = self._sleep_seconds
			schedule_job_change = self._schedule_job_change
			# job__ = schedule_job_change[0]
			day__ = str(schedule_job_change[1]).lower()
			hour__ = schedule_job_change[2]
			minute__ = schedule_job_change[3]
			time__ = '{0}:{1}'.format(hour__, minute__)

			if day__ == 'monday':
				every().monday.at(time__).do(job_func=self.change_job)
			elif day__ == 'tuesday':
				every().tuesday.at(time__).do(job_func=self.change_job)
			elif day__ == 'wednesday':
				every().wednesday.at(time__).do(job_func=self.change_job)
			elif day__ == 'thursday':
				every().thursday.at(time__).do(job_func=self.change_job)
			elif day__ == 'friday':
				every().friday.at(time__).do(job_func=self.change_job)
			elif day__ == 'saturday':
				every().saturday.at(time__).do(job_func=self.change_job)
			elif day__ == 'sunday':
				every().sunday.at(time__).do(job_func=self.change_job)
			else:
				every().day.at(time__).do(job_func=self.change_job)

			while True:
				run_pending()
				time.sleep(sleep_seconds)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	def chain_job(self):
		try:
			return self._custom_upload_data.run()
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	def change_job(self):
		try:
			return self._custom_send_support_message.run()
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None


if __name__ == '__main__':
	Scheduler.__init__(Scheduler())
