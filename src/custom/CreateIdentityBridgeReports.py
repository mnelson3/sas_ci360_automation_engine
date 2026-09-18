#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import csv
import json
from datetime import datetime
from pathlib import Path

from custom import root_path
from log import Log
from connection import Connection
from reporter import Reporter
from security import Security
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'custom-create_identity_bridge_reports.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class CreateIdentityBridgeReports:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			CreateIdentityBridgeReports.__mode = kwargs['mode']
		else:
			CreateIdentityBridgeReports.__mode = None
		self.__mode = CreateIdentityBridgeReports.__mode

		if self.__mode is not None:
			self._reporter = Reporter.Reporter(mode=self.__mode)
			self._standard = Standard.Standard(mode=self.__mode)
			self._external_gateway_path = self._standard.external_gateway_path_arr
			self._identity_bridge_table_id = self._standard.identity_bridge_table_id_arr
			self._report_folder = self._standard.reports_path_arr
			self._secret_key = self._standard.secret_key_arr
			self._tenant_id = self._standard.tenant_id_arr
		else:
			self._reporter = Reporter.Reporter()
			self._standard = Standard.Standard()
			self._report_folder = self._standard.reports_path
			self._external_gateway_path = self._standard.external_gateway_path
			self._identity_bridge_table_id = self._standard.identity_bridge_table_id
			self._secret_key = self._standard.secret_key
			self._tenant_id = self._standard.tenant_id

		self._gDirDataResponseImportRequestJobsGet = self._standard.gDirDataResponseImportRequestJobsGet
		self._import_request_jobs_path = self._standard.import_request_jobs_path
		self._connection = Connection.Connection()
		self._security = Security.Security()

	def run(self, **kwargs):
		try:
			if 'time_stamp' in kwargs:
				time_stamp_ = kwargs['time_stamp']
			else:
				time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
				time_stamp_ = time_stamp.replace(':', '')

			self.refresh_data(time_stamp=time_stamp_)

			if self.__mode is not None:
				folder = '{0}{1}/'.format(self._gDirDataResponseImportRequestJobsGet, self.__mode)
			else:
				folder = '{0}{1}/'.format(self._gDirDataResponseImportRequestJobsGet, 'development')

			report_folder = self._report_folder
			table_id = self._identity_bridge_table_id
			file_name = 'import_request_jobs_get_{}'.format(time_stamp_)
			json_file = Path('{0}{1}{2}{3}'.format(root_path, folder, file_name, '.JSON'))
			csv_file = Path('{0}{1}{2}{3}'.format(root_path, report_folder, file_name, '.CSV'))

			counter = 1
			with open(json_file, 'r', encoding='utf-8') as infile:
				result = json.load(infile)
				if result is not None:
					for item in result['items']:
						if item['dataDescriptorId'] == table_id:
							file_name_ = '{}'.format(item['id'])
							json_file_ = Path('{0}{1}{2}{3}'.format(root_path, folder, file_name_, '.JSON'))
							record = []
							with open(json_file_, 'r', encoding='utf-8') as infile_:
								result_ = json.load(infile_)
								record.append(counter)
								import_validation = result_['statusInfo']['importValidation']
								item_status = import_validation['status']
								record.append(item_status)
								item_start_time = import_validation['startTime']
								record.append(item_start_time)
								item_end_time = import_validation['endTime']
								record.append(item_end_time)
								item_messages = import_validation['messages']
								record.append(item_messages)
								data_processing = result_['statusInfo']['dataProcessing']
								item_status = data_processing['status']
								record.append(item_status)
								item_start_time = data_processing['startTime']
								record.append(item_start_time)
								item_end_time = data_processing['endTime']
								record.append(item_end_time)
								item_messages = data_processing['messages']
								record.append(item_messages)
								identity_processing = result_['statusInfo']['identityProcessing']
								item_status = identity_processing['status']
								record.append(item_status)
								item_start_time = identity_processing['startTime']
								record.append(item_start_time)
								item_end_time = identity_processing['endTime']
								record.append(item_end_time)
								item_messages = identity_processing['messages']
								record.append(item_messages)
								record.append(str(json_file_))

								if item_messages['info'] is not None:
									info_0 = item_messages['info']['Total Number of Records Not Processed']
									record.append(info_0)
									info_1 = item_messages['info']['Total Number of Identities Updated']
									record.append(info_1)
									info_2 = item_messages['info']['Total Number of Identities Created']
									record.append(info_2)
									info_3 = item_messages['info']['Total Number of Identities Rejected']
									record.append(info_3)
									info_4 = item_messages['info']['Total Number of Records Processed']
									record.append(info_4)
								if hasattr(result_, 'failureOutputFiles'):
									failure_output_files = result_['failureOutputFiles']
									failure_output_files_created_time_stamp = failure_output_files["createdTimeStamp"]
									record.append(failure_output_files_created_time_stamp)
									failure_output_files_expires_time_stamp = failure_output_files["expiresTimeStamp"]
									record.append(failure_output_files_expires_time_stamp)
									failure_output_files_http_method = failure_output_files["httpMethod"]
									record.append(failure_output_files_http_method)
									failure_output_files_version = failure_output_files["version"]
									record.append(failure_output_files_version)
									failure_output_files_signed_url = failure_output_files["signedURL"]
									record.append(failure_output_files_signed_url)

								with open(csv_file, 'a', newline='', encoding='utf-8') as outfile:
									writer = csv.writer(outfile, dialect='excel')
									if counter == 1:
										record_header = [
											'No.',
											'importValidationStatus',
											'importValidationStartTime',
											'importValidationEndTime',
											'importValidationMessages',
											'dataProcessingStatus',
											'dataProcessingStartTime',
											'dataProcessingEndTime',
											'dataProcessingMessages',
											'identityProcessingStatus',
											'identityProcessingStartTime',
											'identityProcessingEndTime',
											'identityProcessingMessages',
											'Record Detail',
											'Total Number of Records Not Processed',
											'Total Number of Identities Updated',
											'Total Number of Identities Created',
											'Total Number of Identities Rejected',
											'Total Number of Records Processed',
											'createdTimeStamp',
											'expiresTimeStamp',
											'httpMethod',
											'version',
											'signedURL'
										]
										writer.writerow(record_header)
									writer.writerow(record)
								counter += 1
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return

	def refresh_data(self, **kwargs):
		try:
			if 'time_stamp' in kwargs:
				time_stamp_ = kwargs['time_stamp']
			else:
				time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
				time_stamp_ = time_stamp.replace(':', '')

			if self.__mode is not None:
				folder = '{0}{1}/'.format(self._gDirDataResponseImportRequestJobsGet, self.__mode)
			else:
				folder = '{0}{1}/'.format(self._gDirDataResponseImportRequestJobsGet, 'development')

			external_gateway_path = self._external_gateway_path
			import_request_jobs_path = self._import_request_jobs_path
			secret_key = self._secret_key
			table_id = self._identity_bridge_table_id
			tenant_id = self._tenant_id
			token = self._security.generate_jwt(secret_key=secret_key, tenant_id=tenant_id)

			action = 'GET'
			data = None
			headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
			params = None
			url = 'https://{0}{1}?{2}'.format(external_gateway_path, import_request_jobs_path, 'start=0&limit=999')
			result = self._connection.conn(action=action, data=data, headers=headers, params=params, url=url)
			file_name = 'import_request_jobs_get_{}'.format(time_stamp_)
			self._reporter.store_response(folder=folder, name=file_name, data=result)

			json_file = Path('{0}{1}{2}{3}'.format(root_path, folder, file_name, '.JSON'))

			with open(json_file, 'r', encoding='utf-8') as outfile:
				_result = json.load(outfile)
				_url = None
				if _result is not None:
					for item in _result['items']:
						if item['dataDescriptorId'] == table_id:
							_id = item['id']
							for i in item['links']:
								if i['method'] == 'GET':
									_url = i['href']
									temporary_url = _url
									action = 'GET'
									data = None
									headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
									params = None
									url = temporary_url
									result = self._connection.conn(action=action, data=data, headers=headers, params=params, url=url)
									self._reporter.store_response(folder=folder, name='{}'.format(_id), data=result)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return


if __name__ == '__main__':
	CreateIdentityBridgeReports.__init__(CreateIdentityBridgeReports())
