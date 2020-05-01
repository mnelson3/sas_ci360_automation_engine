#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import os
import time
from pathlib import Path

import requests

from connection import root_path
from log import Log
from security import Security
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'connection.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Connection:
    __instance = None

    @staticmethod
    def get_instance():
        if Connection.__instance is None:
            Connection()
        return Connection.__instance

    def __init__(self, **kwargs):
        if Connection.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            Connection.__instance = self

        standard = Standard.Standard.get_instance()
        security = Security.Security.get_instance()

        self._agent_name = standard.agent_name()
        self._bulk_load_external_events_path = standard.bulk_load_external_events_path()
        self._delimiter = standard.delimiter()
        self._external_gateway = standard.external_gateway()
        self._export_path = standard.export_path()
        self._export_tables_path = standard.export_tables_path()
        self._flag_append = standard.flag_append()
        self._flag_clean_files = standard.flag_clean_files()
        self._flag_csv = standard.flag_csv()
        self._flag_test_export = standard.flag_test_export()
        self._file_transfer_location_path = standard.file_transfer_location_path()
        self._import_base_url = standard.import_base_url()
        self._import_path = standard.import_path()
        self._import_request_jobs_path = standard.import_request_jobs_path()
        self._identity_bridge_table_id = standard.identity_bridge_table_id()
        self._marketing_data_path = standard.marketing_data_path()
        self._marketing_gateway_path = standard.marketing_gateway_path()
        self._schema_version = standard.schema_version()

        self._secret_key = security.secret_key()
        self._tenant_id = security.tenant_id()

        if 'duration' in kwargs:
            self._duration = kwargs['duration']
        if 'end_date_time' in kwargs:
            self._end_date_time = kwargs['end_date_time']
        if 'entity' in kwargs:
            self._entity = kwargs['entity']
        if 'prefix' in kwargs:
            self._prefix = kwargs['prefix']
        if 'report_name' in kwargs:
            self._report_name = kwargs['report_name']
        if 'schema_url' in kwargs:
            self._schema_url = kwargs['schema_url']
        if 'start_date_time' in kwargs:
            self._start_date_time = kwargs['start_date_time']

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

    def entity(self, value=None):
        if value:
            self._entity = value
        try:
            return self._entity
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def prefix(self, value=None):
        if value:
            self._prefix = value
        try:
            return self._prefix
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

    def schema_url(self, value=None):
        if value:
            self._schema_url = value
        try:
            return self._schema_url
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

    def get_discover(self, response=None, **kwargs):
        try:
            ds_dsc_root = Path(root_path + Standard.gDsDscRoot)
            self.clean_data_store(self, ds_dsc_root=ds_dsc_root)

            agent_name = self._agent_name
            schema_version = self._schema_version

            duration = str(self.duration())
            end_date_time = self.end_date_time()
            start_date_time = self.start_date_time()

            external_gateway = self._external_gateway
            export_path = self._export_path
            export_tables_path = self._export_tables_path
            url_get = 'https://{0}{1}{2}'.format(external_gateway, export_path, export_tables_path)

            security = Security.Security.get_instance()
            secret_key = kwargs['secret_key']
            token = security.generate_jwt(secret_key=secret_key)
            headers = {'Authorization': 'Bearer ' + token.decode(), 'Cache-Control': 'no-cache'}

            if duration is not None:
                Standard.gQuerystring['limit'] = duration
            if start_date_time is not None:
                Standard.gQuerystring['dataRangeStartTimeStamp'] = start_date_time
            if end_date_time is not None:
                Standard.gQuerystring['dataRangeEndTimeStamp'] = end_date_time
            Standard.gQuerystring['agentName'] = agent_name[0]
            Standard.gQuerystring['schemaVersion'] = schema_version
            response = requests.get(url=url_get, headers=headers, params=Standard.gQuerystring).text.encode(encoding='UTF-8', errors='replace')
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return response

    def post_bulk_load_external_events(self, result=None, **kwargs):
        try:
            response = None

            external_gateway = self._external_gateway
            marketing_gateway_path = self._marketing_gateway_path
            bulk_load_external_events_path = self._bulk_load_external_events_path
            url_post = 'https://{0}{1}{2}'.format(external_gateway, marketing_gateway_path, bulk_load_external_events_path)

            secret_key = kwargs['secret_key']
            security = Security.Security.get_instance()
            token = security.generate_jwt(secret_key=secret_key)
            headers = {'Authorization': 'Bearer ' + token.decode(), 'Content-Type': 'application/json'}

            payload = '{' \
                      ' "version": 1, ' \
                      ' "applicationId": "eventGenerator" ' \
                      '}'

            code = 500
            while not 200 <= code <= 299:
                logger.info(msg='Checking...')
                time.sleep(15)
                response = requests.post(url=url_post, headers=headers, data=payload)
                code = int(response.status_code)
                response.close()
            result = response
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return result

    def post_file_transfer_location(self, result=None, **kwargs):
        try:
            response = None

            external_gateway = self._external_gateway
            marketing_data_path = self._marketing_data_path
            file_transfer_location_path = self._file_transfer_location_path
            url_post = 'https://{0}{1}{2}'.format(external_gateway, marketing_data_path, file_transfer_location_path)

            secret_key = kwargs['secret_key']
            security = Security.Security.get_instance()
            token = security.generate_jwt(secret_key=secret_key)
            headers = {'Authorization': 'Bearer ' + token.decode(), 'Content-Type': 'application/json'}

            code = 500
            while not 200 <= code <= 299:
                logger.info(msg='Checking...')
                time.sleep(15)
                response = requests.post(url=url_post, headers=headers)
                code = int(response.status_code)
                response.close()
            result = response
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return result

    @staticmethod
    def put_file_location(result=None, **kwargs):
        try:
            response = None

            url_put = kwargs['url_put']
            headers = {'Content-Type': 'application/octet-stream'}
            file_path = kwargs['file_path']

            code = 500
            while not 200 <= code <= 299:
                logger.info(msg='Checking...')
                time.sleep(15)
                response = requests.put(url=url_put, headers=headers, data=open(file_path, 'rb'))
                code = int(response.status_code)
                response.close()
            result = response
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return result

    def get_import_request_jobs(self, result=None, **kwargs):
        try:
            response = None

            external_gateway = self._external_gateway
            import_path = self._import_path
            import_request_jobs_path = self._import_request_jobs_path

            import_request_id = kwargs['import_request_id']

            url_get = 'https://{0}{1}{2}/{3}'.format(external_gateway, import_path, import_request_jobs_path, import_request_id)
            headers = {'Content-Type': 'application/json'}

            code = 500
            while not 200 <= code <= 299:
                logger.info(msg='Checking...')
                time.sleep(15)
                response = requests.get(url=url_get, headers=headers)
                code = int(response.status_code)
                response.close()
            result = response
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return result

    def post_import_request_job(self, result=None, **kwargs):
        try:
            response = None

            external_gateway = self._external_gateway
            import_path = self._import_path
            import_request_jobs_path = self._import_request_jobs_path

            url_post = 'https://{0}{1}{2}'.format(external_gateway, import_path, import_request_jobs_path)

            secret_key = kwargs['secret_key']
            security = Security.Security.get_instance()
            token = security.generate_jwt(secret_key=secret_key)
            headers = {'Authorization': 'Bearer ' + token.decode(), 'Content-Type': 'application/json'}

            table_id = kwargs['table_id']
            temporary_url = kwargs['temporary_url']
            payload = '{' \
                ' "contentName": "Identity Bridge Data", ' \
                ' "dataDescriptorId": "' + table_id + '", ' \
                ' "fieldDelimiter": ",", ' \
                ' "fileLocation": "' + temporary_url + '", ' \
                ' "fileType": "CSV", ' \
                ' "headerRowIncluded": true, ' \
                ' "recordLimit": 0, ' \
                ' "updateMode": "upsert" ' \
                '}'

            code = 500
            while not 200 <= code <= 299:
                logger.info(msg='Checking...')
                time.sleep(15)
                response = requests.post(url=url_post, headers=headers, data=payload)
                code = int(response.status_code)
                response.close()
            result = response
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return result

    @staticmethod
    def clean_data_store(self, response=None, **kwargs):
        try:
            flag_clean_files = self._flag_clean_files
            ds_dsc_root = kwargs['ds_dsc_root']
            if flag_clean_files is True:
                for root, dirs, files in os.walk(ds_dsc_root):
                    for file in files:
                        if file != Standard.Standard.export_test_file(self):
                            os.remove(os.path.join(root, file))
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return response


if __name__ == '__main__':
    Connection.__init__(Connection())
