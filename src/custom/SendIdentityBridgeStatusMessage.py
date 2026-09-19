#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from custom import root_path
from log import Log
from communication import Communication
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'custom-send_identity_bridge_status_message.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class SendIdentityBridgeStatusMessage:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			SendIdentityBridgeStatusMessage.__mode = kwargs['mode']
		else:
			SendIdentityBridgeStatusMessage.__mode = None
		self.__mode = SendIdentityBridgeStatusMessage.__mode

		if self.__mode is not None:
			self._communication = Communication.Communication(mode=self.__mode)
			self._standard = Standard.Standard(mode=self.__mode)
			self._email_msg_from = self._standard.email_msg_status_from_arr
			self._email_msg_to = self._standard.email_msg_status_to_arr
			self._report_path = self._standard.reports_path_arr
		else:
			self._communication = Communication.Communication()
			self._standard = Standard.Standard()
			self._email_msg_from = self._standard.email_msg_status_from
			self._email_msg_to = self._standard.email_msg_status_to
			self._report_path = self._standard.reports_path

	def run(self, **kwargs):
		try:
			time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
			if 'time_stamp' in kwargs:
				message = 'A new chain file was processed today.'
				time_stamp_ = kwargs['time_stamp']
			else:
				message = 'No chain file was processed today.'
				time_stamp_ = time_stamp.replace(':', '')

			email_msg_from = self._email_msg_from
			email_msg_to = self._email_msg_to
			report_folder = self._report_path

			if 'file_name' in kwargs:
				file_name = kwargs['file_name']
				csv_file = Path('{0}{1}{2}{3}'.format(root_path, report_folder, file_name, '.CSV'))
			else:
				file_name = 'import_request_jobs_get_{}'.format(time_stamp_)
				csv_file = Path('{0}{1}{2}{3}'.format(root_path, report_folder, file_name, '.CSV'))

			msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY] <{0}>'.format(email_msg_from)
			msg_to = email_msg_to
			msg_subject = 'Daily Identity Bridge Update [{0}]'.format(time_stamp)
			msg_body = message
			msg_attachment = csv_file

			self._communication.send_email(
				email_msg_from=msg_from,
				email_msg_to=msg_to,
				email_msg_subject=msg_subject,
				email_msg_body=msg_body,
				email_msg_attachment=msg_attachment
			)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return


if __name__ == '__main__':
	SendIdentityBridgeStatusMessage.__init__(SendIdentityBridgeStatusMessage())
