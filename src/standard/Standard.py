#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from log import Log
from standard import root_path

gSql = ''
gSqlInsert = ''
gQuerystring = {}
gSohDelimiter = '\001'
gDirRoot = '/SAS_CI360_Automation_Engine/'
gDirConfig = '/config/'
gDirLog = '/logs/'
gDirReport = '/reports/'
gDirData = '/data/'
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

_log_file_ = Path(root_path + gDirLog + 'standard.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Standard:
	__instance = None

	@staticmethod
	def get_instance():
		if Standard.__instance is None:
			Standard()
		return Standard.__instance

	def __init__(self):
		if Standard.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			Standard.__instance = self
		keys = self.load()
		self._agent_name = str(keys['agent_name']).split(',')
		self._algorithm = keys['algorithm']
		self._bulk_load_external_events_path = keys['bulk_load_external_events_path']
		self._delimiter = keys['delimiter']
		self._discover_service_path = keys['discover_service_path']
		self._duration = keys['duration']
		self._encoding = keys['encoding']
		self._email_from = keys['email_from']
		self._email_to = keys['email_to']
		self._email_server = keys['email_server']
		self._email_server_login = keys['email_server_login']
		self._email_server_password = keys['email_server_password']
		self._email_server_port = keys['email_server_port']
		self._end_date = keys['end_date']
		self._end_date_time = keys['end_date_time']
		self._end_time = keys['end_time']
		self._external_gateway = keys['external_gateway']
		self._export_tables_path = keys['export_tables_path']
		self._export_prod_file = keys['export_prod_file']
		self._export_prod_path = keys['export_prod_path']
		self._export_test_file = keys['export_test_file']
		self._export_test_path = keys['export_test_path']
		self._file_transfer_location_path = keys['file_transfer_location_path']
		self._flag_append = keys['flag_append']
		self._flag_clean_files = keys['flag_clean_files']
		self._flag_csv = keys['flag_csv']
		self._flag_csv_header = keys['flag_csv_header']
		self._flag_test_export = keys['flag_test_export']
		self._flag_test_report = keys['flag_test_report']
		self._identity_bridge_table_id = keys['identity_bridge_table_id']
		self._identity_value = keys['identity_value']
		self._import_base_url = keys['import_base_url']
		self._import_path = keys['import_path']
		self._import_request_jobs_path = keys['import_request_jobs_path']
		self._interval = keys['interval']
		self._marketing_data_path = keys['marketing_data_path']
		self._marketing_gateway_path = keys['marketing_gateway_path']
		self._report_name = str(keys['report_name']).split(',')
		self._schema_version = keys['schema_version']
		self._secret_key = keys['secret_key']
		self._start_date = keys['start_date']
		self._start_date_time = keys['start_date_time']
		self._start_time = keys['start_time']
		self._table_id = keys['table_id']
		self._tenant_id = keys['tenant_id']

	def agent_name(self, value=None):
		if value:
			self._agent_name = value
		try:
			return self._agent_name
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def algorithm(self, value=None):
		if value:
			self._algorithm = value
		try:
			return self._algorithm
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def bulk_load_external_events_path(self, value=None):
		if value:
			self._bulk_load_external_events_path = value
		try:
			return self._bulk_load_external_events_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def delimiter(self, value=None):
		if value:
			self._delimiter = value
		try:
			return self._delimiter
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def duration(self, value=None):
		if value:
			self._duration = value
		try:
			if type(self._duration) == str:
				return int(self._duration)
			return self._duration
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_from(self, value=None):
		if value:
			self._email_from = value
		try:
			return self._email_from
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_to(self, value=None):
		if value:
			self._email_to = value
		try:
			return self._email_to
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_server(self, value=None):
		if value:
			self._email_server = value
		try:
			return self._email_server
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_server_login(self, value=None):
		if value:
			self._email_server_login = value
		try:
			return self._email_server_login
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_server_password(self, value=None):
		if value:
			self._email_server_password = value
		try:
			return self._email_server_password
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def email_server_port(self, value=None):
		if value:
			self._email_server_port = value
		try:
			return self._email_server_port
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def encoding(self, value=None):
		if value:
			self._encoding = value
		try:
			return self._encoding
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def end_date(self, value=None):
		if value:
			self._end_date = value
		try:
			if (type(self._end_date) == str) and (self._end_date == 'None'):
				return None
			return self._end_date
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def end_date_time(self, value=None):
		if value:
			self._end_date_time = value
		try:
			if (type(self._end_date_time) == str) and (self._end_date_time == 'None'):
				return None
			return self._end_date_time
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def end_time(self, value=None):
		if value:
			self._end_time = value
		try:
			if (type(self._end_time) == str) and (self._end_time == 'None'):
				return None
			return self._end_time
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def external_gateway(self, value=None):
		if value:
			self._external_gateway = value
		try:
			return self._external_gateway
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def export_test_file(self, value=None):
		if value:
			self._export_test_file = value
		try:
			return self._export_test_file
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def export_test_path(self, value=None):
		if value:
			self._export_test_path = value
		try:
			return self._export_test_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def export_prod_file(self, value=None):
		if value:
			self._export_prod_file = value
		try:
			return self._export_prod_file
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def export_prod_path(self, value=None):
		if value:
			self._export_prod_path = value
		try:
			return self._export_prod_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def export_tables_path(self, value=None):
		if value:
			self._export_tables_path = value
		try:
			return self._export_tables_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def file_transfer_location_path(self, value=None):
		if value:
			self._file_transfer_location_path = value
		try:
			return self._file_transfer_location_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_append(self, value=None):
		if value:
			self._flag_append = value
		try:
			return bool(self._flag_append)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_clean_files(self, value=None):
		if value:
			self._flag_clean_files = value
		try:
			return bool(self._flag_clean_files)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_csv(self, value=None):
		if value:
			self._flag_csv = value
		try:
			return bool(self._flag_csv)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_csv_header(self, value=None):
		if value:
			self._flag_csv_header = value
		try:
			return bool(self._flag_csv_header)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_test_export(self, value=None):
		if value:
			self._flag_test_export = value
		try:
			return bool(self._flag_test_export)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def flag_test_report(self, value=None):
		if value:
			self._flag_test_report = value
		try:
			return bool(self._flag_test_report)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def identity_bridge_table_id(self, value=None):
		if value:
			self._identity_bridge_table_id = value
		try:
			return self._identity_bridge_table_id
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def identity_value(self, value=None):
		if value:
			self._identity_value = value
		try:
			return self._identity_value
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def interval(self, value=None):
		if value:
			self._interval = value
		try:
			if type(self._interval) == str:
				return int(self._interval)
			return self._interval
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def import_base_url(self, value=None):
		if value:
			self._import_base_url = value
		try:
			return self._import_base_url
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def import_path(self, value=None):
		if value:
			self._import_path = value
		try:
			return self._import_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def import_request_jobs_path(self, value=None):
		if value:
			self._import_request_jobs_path = value
		try:
			return self._import_request_jobs_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def marketing_data_path(self, value=None):
		if value:
			self._marketing_data_path = value
		try:
			return self._marketing_data_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def marketing_gateway_path(self, value=None):
		if value:
			self._marketing_gateway_path = value
		try:
			return self._marketing_gateway_path
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def report_name(self, value=None):
		if value:
			self._report_name = value
		try:
			return self._report_name
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def schema_version(self, value=None):
		if value:
			self._schema_version = value
		try:
			return self._schema_version
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def secret_key(self, value=None):
		if value:
			self._secret_key = value
		try:
			return self._secret_key
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def start_date(self, value=None):
		if value:
			self._start_date = value
		try:
			if (type(self._start_date) == str) and (self._start_date == 'None'):
				return None
			return self._start_date
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def start_date_time(self, value=None):
		if value:
			self._start_date_time = value
		try:
			if (type(self._start_date_time) == str) and (self._start_date_time == 'None'):
				return None
			return self._start_date_time
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def start_time(self, value=None):
		if value:
			self._start_time = value
		try:
			if (type(self._start_time) == str) and (self._start_time == 'None'):
				return None
			return self._start_time
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def table_id(self, value=None):
		if value:
			self._table_id = value
		try:
			return self._table_id
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def tenant_id(self, value=None):
		if value:
			self._tenant_id = value
		try:
			return self._tenant_id
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	@staticmethod
	def load():
		keys = {}
		try:
			config_file = Path(root_path + gDirConfig + 'config.txt')
			separator = '='
			with open(config_file) as f:
				for line in f:
					if not line.startswith('#'):
						if separator in line:
							name, value = line.split(separator, 1)
							keys[name.strip()] = value.strip()
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None
		finally:
			return keys

	@staticmethod
	def get_date_time_stamp():
		result = datetime.now().strftime('%Y%m%d%H%M%S')
		return result


if __name__ == '__main__':
	Standard.__init__(Standard())
