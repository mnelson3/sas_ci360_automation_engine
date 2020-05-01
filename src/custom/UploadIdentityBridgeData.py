#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from communication import Communication
from connection import Connection
from custom import root_path
from log import Log
from reporter import Reporter
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'custom-upload_identity_bridge_data.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class UploadIdentityBridgeData:
	__instance = None

	@staticmethod
	def get_instance():
		if UploadIdentityBridgeData.__instance is None:
			UploadIdentityBridgeData()
		return UploadIdentityBridgeData.__instance

	def __init__(self):
		if UploadIdentityBridgeData.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			UploadIdentityBridgeData.__instance = self

		standard = Standard.Standard.get_instance()

		self._flag_test_export = standard.flag_test_export()
		self._flag_test_report = standard.flag_test_report()
		self._suppression_email_domain_list = standard.suppression_email_domain_list()
		self._suppression_form_name_list = standard.suppression_form_name_list()

	@staticmethod
	def run(result=None):
		try:
			communication = Communication.Communication.get_instance()
			connection = Connection.Connection.get_instance()
			reporter = Reporter.Reporter.get_instance()
			standard = Standard.Standard.get_instance()

			time_stamp = standard.get_date_time_stamp()
			secret_key = standard.secret_key()

			# POST to fileTransferLocation - no payload
			connection.post_file_transfer_location(result=result, secret_key=secret_key)
			reporter.build_report(prefix=time_stamp, name='post_file_transfer_location', json_response=result)

			url_put = None
			if result is not None:
				for item in result:
					url_put = item['signedURL']

				if standard.flag_test_export() is True:
					file_path = Path(root_path + standard.export_test_path() + standard.export_test_file())
				else:
					file_path = Path(root_path + standard.export_prod_path() + standard.export_prod_file())

				# PUT to temporary URL
				connection.put_file_location(result=result, url_put=url_put, file_path=file_path)
				reporter.build_report(prefix=time_stamp, name='put_file_location', json_response=result)

			# POST to importRequestJobs - set payload [TABLE_ID] and [TEMPORARY_URL]
			table_id = standard.table_id()
			connection.post_import_request_job(result=result, secret_key=secret_key, table_id=table_id, temporary_url=url_put)
			reporter.build_report(prefix=time_stamp, name='post_import_request_job', json_response=result)

			import_request_id = None
			for item in result:
				import_request_id = item['id']

			# GET from importRequestJobs - [IMPORT_REQUEST_ID]
			connection.get_import_request_jobs(result=result, secret_key=secret_key, import_request_id=import_request_id)
			reporter.build_report(prefix=time_stamp, name='get_import_request_jobs', json_response=result)

			# GET from importRequestJobs - failureOutputFiles
			for item in result:
				if item['failureOutputFiles'] is not None:
					for i in item['failureOutputFiles']:
						import_request_id = i['url']

			connection.get_import_request_jobs(result=result, secret_key=secret_key, import_request_id=import_request_id)
			reporter.build_report(prefix=time_stamp, name='get_import_request_jobs', json_response=result)

			msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY]'
			msg_to = 'Mark.Nelson@sas.com'
			msg_subject = 'Daily Identity Bridge Update: {}'.format(time_stamp)
			communication.send_email(msg_from=msg_from, msg_to=msg_to, msg_subject=msg_subject)
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None
		finally:
			return


if __name__ == '__main__':
	UploadIdentityBridgeData.__init__(UploadIdentityBridgeData())
