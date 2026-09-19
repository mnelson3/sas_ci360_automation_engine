#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import configparser
from configparser import ConfigParser
from pathlib import Path

from log import Log
from standard import root_path

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'standard.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Standard:
	__mode = None

	gSql = ''
	gSqlInsert = ''
	gQuerystring = {}
	gSohDelimiter = '\001'
	gDirRoot = '/SAS_CI360_Automation_Engine/'
	gDirConfig = '/config/'
	gDirLog = '/logs/'
	gDirData = '/data/'
	gDirDataResponse = '/data/response/'
	gDirDataResponseAnalyticGet = '/data/response/analytic_get/'
	gDirDataResponseAnalyticPost = '/data/response/analytic_post/'
	gDirDataResponseAnalyticTransfersPost = '/data/response/analytic_transfers_post/'
	gDirDataResponseBulkLoadExternalEventsPost = '/data/response/bulk_load_external_events_post/'
	gDirDataResponseCustomerJobsGet = '/data/response/customer_jobs_get/'
	gDirDataResponseCustomerJobsPost = '/data/response/customer_jobs_post/'
	gDirDataResponseEventJobsGet = '/data/response/event_jobs_get/'
	gDirDataResponseEventJobsPost = '/data/response/event_jobs_post/'
	gDirDataResponseExportRequestJobsGet = '/data/response/export_request_jobs_get/'
	gDirDataResponseExportRequestJobsPost = '/data/response/export_request_jobs_post/'
	gDirDataResponseFileTransferLocationPost = '/data/response/file_transfer_location_post/'
	gDirDataResponseIdentityRecordsGet = '/data/response/identity_records_get/'
	gDirDataResponseImportRequestJobsGet = '/data/response/import_request_jobs_get/'
	gDirDataResponseImportRequestJobsPost = '/data/response/import_request_jobs_post/'
	gDirDataResponseTablesGet = '/data/response/tables_get/'
	gDirDataResponseTablesPost = '/data/response/tables_post/'
	gDsDscRoot = '/data/discover/'
	gDsDscClean = '/data/discover/clean/'
	gDsDscConfig = '/data/discover/dsccnfg/'
	gDsDscZip = '/data/discover/dscdonl/'
	gDsDscExtr = '/data/discover/dscextr/'
	gDsDscCsv = '/data/discover/dscwh/'
	gDsDscExport = '/data/discover/export/'
	gDsDscFix = '/data/discover/fix/'
	gDsDscSql = '/data/discover/sql/'
	gDsEngRoot = '/data/engage/'
	gDsEngDownload = '/data/engage/download/'
	gDsEngExport = '/data/engage/export/'
	gDsEngJson = '/data/engage/json/'
	gDsEngProcessA = '/data/engage/process_a/'
	gDsEngProcessB = '/data/engage/process_b/'
	gDsEngProcessC = '/data/engage/process_c/'
	gDsEngProcessD = '/data/engage/process_d/'
	gDsEngProcessE = '/data/engage/process_e/'
	gDsEngProcessF = '/data/engage/process_f/'

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Standard.__mode = kwargs['mode']
		else:
			Standard.__mode = None
		self.__mode = Standard.__mode

		config_parser = ConfigParser(interpolation=configparser.ExtendedInterpolation())
		config_file = Path('{0}{1}{2}'.format(root_path, '/config/', 'config.ini'))
		config_parser.read(config_file)

		# DATETIME
		self._duration = config_parser.get('DATETIME', 'duration')
		self._end_date = config_parser.get('DATETIME', 'end_date')
		self._end_date_time = config_parser.get('DATETIME', 'end_date_time')
		self._end_time = config_parser.get('DATETIME', 'end_time')
		self._interval_hours = config_parser.get('DATETIME', 'interval_hours')
		self._interval_minutes = config_parser.get('DATETIME', 'interval_minutes')
		self._schedule_job_arr = config_parser.get('DATETIME', 'schedule_job_arr')
		self._schedule_job_chain = config_parser.get('DATETIME', 'schedule_job_chain')
		self._schedule_job_change = config_parser.get('DATETIME', 'schedule_job_change')
		self._sleep_seconds = config_parser.get('DATETIME', 'sleep_seconds')
		self._start_date = config_parser.get('DATETIME', 'start_date')
		self._start_date_time = config_parser.get('DATETIME', 'start_date_time')
		self._start_time = config_parser.get('DATETIME', 'start_time')

		# EMAIL
		self._email_msg_status_from_arr = config_parser.get('EMAIL', 'email_msg_status_from_arr')
		self._email_msg_status_from = config_parser.get('EMAIL', 'email_msg_status_from')
		self._email_msg_status_to_arr = config_parser.get('EMAIL', 'email_msg_status_to_arr')
		self._email_msg_status_to = config_parser.get('EMAIL', 'email_msg_status_to')
		self._email_msg_support_from_arr = config_parser.get('EMAIL', 'email_msg_support_from_arr')
		self._email_msg_support_from = config_parser.get('EMAIL', 'email_msg_support_from')
		self._email_msg_support_to_arr = config_parser.get('EMAIL', 'email_msg_support_to_arr')
		self._email_msg_support_to = config_parser.get('EMAIL', 'email_msg_support_to')
		self._email_msg_support_cc_arr = config_parser.get('EMAIL', 'email_msg_support_cc_arr')
		self._email_msg_support_cc = config_parser.get('EMAIL', 'email_msg_support_cc')
		self._email_server_arr = config_parser.get('EMAIL', 'email_server_arr')
		self._email_server = config_parser.get('EMAIL', 'email_server')
		self._email_server_login_arr = config_parser.get('EMAIL', 'email_server_login_arr')
		self._email_server_login = config_parser.get('EMAIL', 'email_server_login')
		self._email_server_password_arr = config_parser.get('EMAIL', 'email_server_password_arr')
		self._email_server_password = config_parser.get('EMAIL', 'email_server_password')
		self._email_server_port_arr = config_parser.get('EMAIL', 'email_server_port_arr')
		self._email_server_port = config_parser.get('EMAIL', 'email_server_port')

		# FILES
		self._file_export_arr = config_parser.get('FILES', 'file_export_arr')
		self._file_export = config_parser.get('FILES', 'file_export')
		self._file_change_export_arr = config_parser.get('FILES', 'file_change_export_arr')
		self._file_change_export = config_parser.get('FILES', 'file_change_export')

		# FLAGS
		self._flag_append = config_parser.get('FLAGS', 'flag_append')
		self._flag_clean_files = config_parser.get('FLAGS', 'flag_clean_files')
		self._flag_csv = config_parser.get('FLAGS', 'flag_csv')
		self._flag_csv_header = config_parser.get('FLAGS', 'flag_csv_header')
		self._flag_test_export = config_parser.get('FLAGS', 'flag_test_export')
		self._flag_test_report = config_parser.get('FLAGS', 'flag_test_report')

		# IDENTITIES
		self._identity_bridge_table_id_arr = config_parser.get('IDENTITIES', 'identity_bridge_table_id_arr')
		self._identity_bridge_table_id = config_parser.get('IDENTITIES', 'identity_bridge_table_id')
		self._identity_value = config_parser.get('IDENTITIES', 'identity_value')
		self._secret_key_arr = config_parser.get('IDENTITIES', 'secret_key_arr')
		self._secret_key = config_parser.get('IDENTITIES', 'secret_key')
		self._tenant_id_arr = config_parser.get('IDENTITIES', 'tenant_id_arr')
		self._tenant_id = config_parser.get('IDENTITIES', 'tenant_id')

		# PATHS
		self._path_analytic_services_controller = config_parser.get('PATHS', 'path_analytic_services_controller')
		self._path_analytic_transfer_controller = config_parser.get('PATHS', 'path_analytic_transfer_controller')
		self._path_bulk_load_external_events = config_parser.get('PATHS', 'path_bulk_load_external_events')
		self._path_customer_jobs = config_parser.get('PATHS', 'path_customer_jobs')
		self._path_discover_service = config_parser.get('PATHS', 'path_discover_service')
		self._path_event_jobs = config_parser.get('PATHS', 'path_event_jobs')
		self._path_export_arr = config_parser.get('PATHS', 'path_export_arr')
		self._path_export = config_parser.get('PATHS', 'path_export')
		self._path_export_post_arr = config_parser.get('PATHS', 'path_export_post_arr')
		self._path_export_post = config_parser.get('PATHS', 'path_export_post')
		self._path_export_request_jobs = config_parser.get('PATHS', 'path_export_request_jobs')
		self._path_export_tables = config_parser.get('PATHS', 'path_export_tables')
		self._path_external_gateway_arr = config_parser.get('PATHS', 'path_external_gateway_arr')
		self._path_external_gateway = config_parser.get('PATHS', 'path_external_gateway')
		self._path_file_transfer_location = config_parser.get('PATHS', 'path_file_transfer_location')
		self._path_identity_records = config_parser.get('PATHS', 'path_identity_records')
		self._path_import = config_parser.get('PATHS', 'path_import')
		self._path_import_request_jobs = config_parser.get('PATHS', 'path_import_request_jobs')
		self._path_marketing_data = config_parser.get('PATHS', 'path_marketing_data')
		self._path_marketing_gateway = config_parser.get('PATHS', 'path_marketing_gateway')
		self._path_reports_arr = config_parser.get('PATHS', 'path_reports_arr')
		self._path_reports = config_parser.get('PATHS', 'path_reports')
		# self._path_root = config_parser.get('PATHS', 'path_root')
		self._path_tables = config_parser.get('PATHS', 'path_tables')

		# SETTINGS
		self._agent_name_arr = config_parser.get('SETTINGS', 'agent_name_arr')
		self._agent_name = config_parser.get('SETTINGS', 'agent_name')
		self._algorithm = config_parser.get('SETTINGS', 'algorithm')
		self._delimiter = config_parser.get('SETTINGS', 'delimiter')
		self._encoding = config_parser.get('SETTINGS', 'encoding')
		self._dataset_name_arr = config_parser.get('SETTINGS', 'dataset_name_arr')
		self._dataset_name = config_parser.get('SETTINGS', 'dataset_name')
		self._mode_name_arr = config_parser.get('SETTINGS', 'mode_name_arr')
		self._schema_version = config_parser.get('SETTINGS', 'schema_version')
		self._tenant_environment_arr = config_parser.get('SETTINGS', 'tenant_environment_arr')
		self._tenant_environment = config_parser.get('SETTINGS', 'tenant_environment')
		self._tenant_name_arr = config_parser.get('SETTINGS', 'tenant_name_arr')
		self._tenant_name = config_parser.get('SETTINGS', 'tenant_name')
		self._tenant_number_arr = config_parser.get('SETTINGS', 'tenant_number_arr')
		self._tenant_number = config_parser.get('SETTINGS', 'tenant_number')
		self._tenant_product_arr = config_parser.get('SETTINGS', 'tenant_product_arr')
		self._tenant_product = config_parser.get('SETTINGS', 'tenant_product')
		self._tenant_url_arr = config_parser.get('SETTINGS', 'tenant_url_arr')
		self._tenant_url = config_parser.get('SETTINGS', 'tenant_url')

	@property
	def agent_name_arr(self):
		try:
			result = str(self._agent_name_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def agent_name(self):
		try:
			return self._agent_name
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def algorithm(self):
		try:
			return self._algorithm
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def analytic_services_controller_path(self):
		try:
			return self._path_analytic_services_controller
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def analytic_transfer_controller_path(self):
		try:
			return self._path_analytic_transfer_controller
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def bulk_load_external_events_path(self):
		try:
			return self._path_bulk_load_external_events
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def customer_jobs_path(self):
		try:
			return self._path_customer_jobs
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def dataset_name_arr(self):
		try:
			result = str(self._dataset_name_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def dataset_name(self):
		try:
			return self._dataset_name
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def delimiter(self):
		try:
			return self._delimiter
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def discover_service_path(self):
		try:
			return self._path_discover_service
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def duration(self):
		try:
			if type(self._duration) == str:
				return int(self._duration)
			return self._duration
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_status_from_arr(self):
		try:
			result = str(self._email_msg_status_from_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_status_from(self):
		try:
			return self._email_msg_status_from
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_status_to_arr(self):
		try:
			result = str(self._email_msg_status_to_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_status_to(self):
		try:
			return self._email_msg_status_to
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_from_arr(self):
		try:
			result = str(self._email_msg_support_from_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_from(self):
		try:
			return self._email_msg_support_from
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_to_arr(self):
		try:
			result = str(self._email_msg_support_to_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_to(self):
		try:
			return self._email_msg_support_to
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_cc_arr(self):
		try:
			result = str(self._email_msg_support_cc_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_msg_support_cc(self):
		try:
			return self._email_msg_support_cc
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_arr(self):
		try:
			result = str(self._email_server_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server(self):
		try:
			return self._email_server
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_login_arr(self):
		try:
			result = str(self._email_server_login_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_login(self):
		try:
			return self._email_server_login
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_password_arr(self):
		try:
			result = str(self._email_server_password_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_password(self):
		try:
			return self._email_server_password
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_port_arr(self):
		try:
			result = str(self._email_server_port_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_port(self):
		try:
			return self._email_server_port
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def encoding(self):
		try:
			return self._encoding
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def end_date(self):
		try:
			if (type(self._end_date) == str) and (self._end_date == 'None'):
				return None
			return self._end_date
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def end_date_time(self):
		try:
			if (type(self._end_date_time) == str) and (self._end_date_time == 'None'):
				return None
			return self._end_date_time
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def end_time(self):
		try:
			if (type(self._end_time) == str) and (self._end_time == 'None'):
				return None
			return self._end_time
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def event_jobs_path(self):
		try:
			return self._path_event_jobs
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_file_arr(self):
		try:
			result = str(self._file_export_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_file(self):
		try:
			return self._file_export
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_change_file_arr(self):
		try:
			result = str(self._file_change_export_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_change_file(self):
		try:
			return self._file_change_export
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_path_arr(self):
		try:
			result = str(self._path_export_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_path(self):
		try:
			return self._path_export
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_post_path_arr(self):
		try:
			result = str(self._path_export_post_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_post_path(self):
		try:
			return self._path_export_post
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_request_jobs_path(self):
		try:
			return self._path_export_request_jobs
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def export_tables_path(self):
		try:
			return self._path_export_tables
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def external_gateway_path_arr(self):
		try:
			result = str(self._path_external_gateway_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def external_gateway_path(self):
		try:
			return self._path_external_gateway
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def file_transfer_location_path(self):
		try:
			return self._path_file_transfer_location
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_append(self):
		try:
			return bool(self._flag_append)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_clean_files(self):
		try:
			return bool(self._flag_clean_files)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_csv(self):
		try:
			return bool(self._flag_csv)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_csv_header(self):
		try:
			return bool(self._flag_csv_header)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_test_export(self):
		try:
			return bool(self._flag_test_export)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def flag_test_report(self):
		try:
			return bool(self._flag_test_report)
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def identity_bridge_table_id_arr(self):
		try:
			result = str(self._identity_bridge_table_id_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def identity_bridge_table_id(self):
		try:
			return self._identity_bridge_table_id
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def identity_records_path(self):
		try:
			return self._path_identity_records
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def identity_value(self):
		try:
			return self._identity_value
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def import_path(self):
		try:
			return self._path_import
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def import_request_jobs_path(self):
		try:
			return self._path_import_request_jobs
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def interval_hours(self):
		try:
			if type(self._interval_hours) == str:
				return int(self._interval_hours)
			return self._interval_hours
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def interval_minutes(self):
		try:
			return self._interval_minutes
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def marketing_data_path(self):
		try:
			return self._path_marketing_data
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def marketing_gateway_path(self):
		try:
			return self._path_marketing_gateway
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def mode_name_arr(self):
		try:
			result = str(self._mode_name_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def reports_path_arr(self):
		try:
			result = str(self._path_reports_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def reports_path(self):
		try:
			return self._path_reports
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def schedule_job_arr(self):
		try:
			result = self._schedule_job_arr.split(',')
			return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def schedule_job_chain(self):
		try:
			result = self._schedule_job_chain.split(',')
			return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def schedule_job_change(self):
		try:
			result = self._schedule_job_change.split(',')
			return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def schema_version(self):
		try:
			return self._schema_version
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def secret_key_arr(self):
		try:
			result = str(self._secret_key_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def secret_key(self):
		try:
			return self._secret_key
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def sleep_seconds(self):
		try:
			if type(self._sleep_seconds) == str:
				return int(self._sleep_seconds)
			return self._sleep_seconds
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def start_date(self):
		try:
			if (type(self._start_date) == str) and (self._start_date == 'None'):
				return None
			return self._start_date
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def start_date_time(self):
		try:
			if (type(self._start_date_time) == str) and (self._start_date_time == 'None'):
				return None
			return self._start_date_time
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def start_time(self):
		try:
			if (type(self._start_time) == str) and (self._start_time == 'None'):
				return None
			return self._start_time
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tables_path(self):
		try:
			return self._path_tables
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_id_arr(self):
		try:
			result = str(self._tenant_id_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_id(self):
		try:
			return self._tenant_id
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_environment_arr(self):
		try:
			result = str(self._tenant_environment_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_environment(self):
		try:
			return self._tenant_environment
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_name_arr(self):
		try:
			result = str(self._tenant_name_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_name(self):
		try:
			return self._tenant_name
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_number_arr(self):
		try:
			result = str(self._tenant_number_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_number(self):
		try:
			return self._tenant_number
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_product_arr(self):
		try:
			result = str(self._tenant_product_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_product(self):
		try:
			return self._tenant_product
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_url_arr(self):
		try:
			result = str(self._tenant_url_arr).split(',')
			if self.__mode == 'development':
				return result[0]
			elif self.__mode == 'test':
				return result[1]
			elif self.__mode == 'production':
				return result[2]
			else:
				return result
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def tenant_url(self):
		try:
			return self._tenant_url
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None


if __name__ == '__main__':
	Standard.__init__(Standard())
