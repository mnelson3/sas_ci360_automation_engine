#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import json
from datetime import datetime
from pathlib import Path

from connection import Connection
from reporter import Reporter
from security import Security
from standard import Standard

__connection = Connection.Connection()
__reporter = Reporter.Reporter()
__security = Security.Security()
__standard = Standard.Standard()

__time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
__secret_key = __standard.secret_key
__tenant_id = __standard.tenant_id
__prod_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6IjA1OTg2ODRhMDYwMDAxMGUyZWIyNDcxNCJ9.SPzyznE2MAdXOgXG7AIKr2ueWXJR5VcvTK5xlFf9cbQ'
__qa_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMiJ9.4yCXGMeCm1aGTt66YLaYppUXnXpq2v6ZjnSSGC-V7s4'
__test_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'
__token = __test_token


def test_tables_get():
	time_stamp = __time_stamp.replace(':', '')
	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
	assert token == __token

	action = 'GET'
	assert action == 'GET'
	data = None
	assert data is None
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
	params = None
	assert params is None
	url = 'https://{0}'.format(__standard.tables_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/tables'
	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	folder = __standard.gDirDataResponseTablesGet
	__reporter.store_response(folder=folder, name='table_get_{}'.format(time_stamp), data=result)


def test_tables_by_id_get():
	time_stamp = __time_stamp.replace(':', '')
	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
	assert token == __token

	table_id = __standard.identity_bridge_table_id
	assert table_id == __standard.identity_bridge_table_id

	file_name = 'table_get_{}'.format(time_stamp)
	json_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', __standard.gDirDataResponseTablesGet, file_name, '.JSON'))

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
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
	params = None
	assert params is None
	url = temporary_url
	assert url == 'https://{0}/{1}'.format(__standard.tables_path(), table_id)
	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	folder = __standard.gDirDataResponseTablesGet
	__reporter.store_response(folder=folder, name='{}'.format(table_id), data=result)


def test_import_request_jobs_get():
	time_stamp = __time_stamp.replace(':', '')
	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
	assert token == __token

	action = 'GET'
	assert action == 'GET'
	data = None
	assert data is None
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
	params = None
	assert params is None
	url = 'https://{0}?{1}'.format(__standard.import_request_jobs_path, 'start=0&limit=999')
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs?start=0&limit=999'
	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	folder = __standard.gDirDataResponseImportRequestJobsGet
	__reporter.store_response(folder=folder, name='import_request_jobs_get_{}'.format(time_stamp), data=result)


# def test_import_request_jobs_by_id_get():
# 	time_stamp = __time_stamp.replace(':', '')
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	table_id = __standard.identity_bridge_table_id()
# 	assert table_id == __standard.identity_bridge_table_id()
#
# 	file_name = 'import_request_jobs_get_{}'.format(time_stamp)
# 	json_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', __standard.gDirDataResponseImportRequestJobsGet, file_name, '.JSON'))
# 	print('json_file = {}'.format(json_file))
#
# 	with open(json_file, 'r', encoding='utf-8') as outfile:
# 		result = json.load(outfile)
# 		__url = None
# 		if result is not None:
# 			for item in result['items']:
# 				if item['dataDescriptorId'] == table_id:
# 					__id = item['id']
# 					for i in item['links']:
# 						if i['method'] == 'GET':
# 							__url = i['href']
# 							print('__url = {0}'.format(__url))
# 							temporary_url = __url
# 							assert temporary_url is not None and temporary_url == __url
#
# 							action = 'GET'
# 							assert action == 'GET'
# 							data = None
# 							assert data is None
# 							headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 							assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 							params = None
# 							assert params is None
# 							url = temporary_url
# 							assert url == 'https://{0}/{1}'.format(__standard.import_request_jobs_path(), __id)
# 							result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 							assert result is not None
# 							folder = __standard.gDirDataResponseImportRequestJobsGet
# 							__reporter.store_response(folder=folder, name='{}'.format(__id), data=result)


# def test_import_request_jobs_post():
# 	time_stamp = __time_stamp.replace(':', '')
# 	content_name = __standard.export_file()
# 	assert content_name is not None
#
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	action = 'POST'
# 	assert action == 'POST'
# 	data = None
# 	assert data is None
# 	headers = {'Authorization': 'Bearer {0}'.format(token), 'Content-Type': 'application/json'}
# 	assert headers == {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo', 'Content-Type': 'application/json'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}'.format(__standard.file_transfer_location_path())
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/fileTransferLocation'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
#
# 	json_file = Path('{0}{1}{2}{3}'.format('D:/Clients/Example_Financial/SAS_CI360_Automation_Engine', Standard.gDirReport, 'test_post_import_request_job_path_1', '.JSON'))
# 	print('json_file = {0}'.format(json_file))
# 	with open(json_file, 'w', encoding='utf-8') as outfile:
# 		json.dump(result, outfile, ensure_ascii=False, indent=4)
# 	__reporter.build_report(name='test_post_import_request_job_path_1', data=result)
#
# 	json_file = Path('{0}{1}{2}{3}'.format('D:/Clients/Example_Financial/SAS_CI360_Automation_Engine', __standard.gDirDataResponseImportRequestJobsGet, 'test_put_file_location_path_2', '.JSON'))
# 	print('json_file = {0}'.format(json_file))
# 	with open(json_file, 'r', encoding='utf-8') as infile:
# 		result = json.load(infile)
#
# 	table_id = __standard.identity_bridge_table_id()
# 	assert table_id == __standard.identity_bridge_table_id()
# 	__signed_url = None
# 	if result is not None:
# 		__signed_url = result['signedURL']
# 	temporary_url = __signed_url
# 	assert temporary_url is not None and temporary_url == __signed_url
#
# 	action = 'POST'
# 	assert action == 'POST'
# 	json_string = """
# 		{
# 			"contentName": "",
# 			"dataDescriptorId": "",
# 			"fieldDelimiter": ",",
# 			"fileLocation": "",
# 			"fileType": "csv",
# 			"headerRowIncluded": true,
# 			"recordLimit": 0,
# 			"updateMode": "upsert"
# 		}"""
# 	data = json.loads(json_string)
# 	data["contentName"] = content_name
# 	data["dataDescriptorId"] = table_id
# 	data["fileLocation"] = temporary_url
# 	print('data = {0}'.format(data))
# 	headers = {'Authorization': 'Bearer {0}'.format(token), 'Content-Type': 'application/json'}
# 	assert headers == {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo', 'Content-Type': 'application/json'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}'.format(__standard.import_request_jobs_path())
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
#
# 	json_file = Path('{0}{1}{2}{3}'.format('D:/Clients/Example_Financial/SAS_CI360_Automation_Engine', __standard.gDirDataResponseImportRequestJobsGet, 'test_post_import_request_job_path', '.JSON'))
# 	print('json_file = {0}'.format(json_file))
# 	with open(json_file, 'w', encoding='utf-8') as outfile:
# 		json.dump(result, outfile, ensure_ascii=False, indent=4)
# 	__reporter.build_report(name='test_post_import_request_job_path', data=result)


# def test_import_request_jobs_get():
# 	time_stamp = __time_stamp.replace(':', '')
# 	__reporter.report_data()
#
# 	action = 'GET'
# 	assert action == 'GET'
# 	data = None
# 	assert data is None
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(__token)}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}?{1}'.format(__standard.import_request_jobs_path(), 'start=0&limit=999')
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs?start=0&limit=999'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
# 	folder = __standard.gDirDataResponseImportRequestJobsGet
# 	__reporter.store_response(folder=folder, name='import_request_jobs_get_{}'.format(time_stamp), data=result)
#
# 	__file_location = []
# 	if result is not None:
# 		for item in result['items']:
# 			# if item['name'] == 'Identity Bridge Data':
# 			__file_location.append(item['fileLocation'])
# 			print('__file_location = {0}'.format(item['fileLocation']))
# 	temporary_url = __file_location[0]
# 	assert temporary_url is not None and temporary_url == __file_location[0]
#
# 	action = 'POST'
# 	assert action == 'POST'
# 	json_string = """
# 		{
# 			"contentName": "",
# 			"dataDescriptorId": "",
# 			"fieldDelimiter": ",",
# 			"fileLocation": "",
# 			"fileType": "csv",
# 			"headerRowIncluded": true,
# 			"recordLimit": 0,
# 			"updateMode": "upsert"
# 		}"""
# 	data = json.loads(json_string)
# 	data["contentName"] = file_export
# 	data["dataDescriptorId"] = table_id
# 	data["fileLocation"] = temporary_url
# 	print('data = {0}'.format(data))
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}'.format(__standard.import_request_jobs_path())
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
#
# 	json_file = Path('{0}{1}{2}{3}'.format('D:/Clients/Example_Financial/SAS_CI360_Automation_Engine', Standard.gDirReport, 'test_put_file_location_path_3', '.JSON'))
# 	print('json_file = {0}'.format(json_file))
# 	with open(json_file, 'w', encoding='utf-8') as outfile:
# 		json.dump(result, outfile, ensure_ascii=False, indent=4)
# 	__reporter.build_report(name='test_put_file_location_path_3', data=result)


# def test_import_request_jobs_by_id_download_failures_get():
# 	time_stamp = __time_stamp.replace(':', '')
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	table_id = __standard.identity_bridge_table_id()
# 	assert table_id == __standard.identity_bridge_table_id()
#
# 	file_name = 'import_request_jobs_get_{}'.format(time_stamp)
# 	json_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', __standard.gDirDataResponseImportRequestJobsGet, file_name, '.JSON'))
# 	print('json_file = {}'.format(json_file))
#
# 	with open(json_file, 'r', encoding='utf-8') as outfile:
# 		result = json.load(outfile)
# 		__url = None
# 		if result is not None:
# 			for item in result['items']:
# 				if item['dataDescriptorId'] == table_id:
# 					__id = item['id']
# 					file_name_ = '{}'.format(__id)
# 					json_file_ = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', __standard.gDirDataResponseImportRequestJobsGet, file_name_, '.JSON'))
# 					print('json_file_ = {}'.format(json_file_))
# 					with open(json_file_, 'r', encoding='utf-8') as outfile_:
# 						result_ = json.load(outfile_)
# 						if result_ is not None:
# 							if result_['status'] == 'Imported':
# 								for item_ in result_['failureOutputFiles']:
# 									if item_ is not None:
# 										__url = item_['signedURL']
# 									print('__url = {}'.format(__url))
# 									action = 'GET'
# 									assert action == 'GET'
# 									data = None
# 									assert data is None
# 									headers = {'Accept': 'application/json', 'Content-Type': 'application/csv'}
# 									assert headers == {'Accept': 'application/json', 'Content-Type': 'application/csv'}
# 									params = None
# 									assert params is None
# 									url = __url
# 									assert url == __url
# 									result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 									assert result is not None
# 									folder = __standard.gDirDataResponseImportRequestJobsGet
# 									__reporter.store_response(folder=folder, name='{}'.format(__id), data=result)


# def test_import_request_jobs_post():
# 	time_stamp = __time_stamp.replace(':', '')
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	action = 'GET'
# 	assert action == 'GET'
# 	data = None
# 	assert data is None
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}?{1}'.format(__standard.import_request_jobs_path(), 'start=0&limit=999')
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs?start=0&limit=999'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
# 	__reporter.store_response(name='test_get_import_request_jobs_{}'.format(time_stamp), data=result)
#
# 	if result is not None:
# 		for item in result['items']:
# 			if item['name'] == 'Identity Bridge Data':
# 				__data_descriptor_id = item['dataDescriptorId']
# 				print('__data_descriptor_id = {0}'.format(__data_descriptor_id))
# 				__data_table_id = item['dataTableId']
# 				print('__data_table_id = {0}'.format(__data_table_id))
# 				__id = item['id']
# 				print('__id = {0}'.format(__id))
# 				__file_location = item['fileLocation']
#
# 				action = 'POST'
# 				assert action == 'POST'
# 				json_string = """
# 					{
# 						"contentName": "",
# 						"dataDescriptorId": "",
# 						"fieldDelimiter": ",",
# 						"fileLocation": "",
# 						"fileType": "CSV",
# 						"headerRowIncluded": "",
# 						"recordLimit": 0,
# 						"updateMode": "upsert"
# 					}"""
# 				data = json.loads(json_string)
# 				data["contentName"] = 'Identity Bridge Data'
# 				data["dataDescriptorId"] = __data_descriptor_id
# 				data["fileLocation"] = __file_location
# 				data["headerRowIncluded"] = True
# 				print('data = {0}'.format(data))
# 				data = None
# 				headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 				assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 				params = None
# 				assert params is None
# 				url = 'https://{0}'.format(__standard.import_request_jobs_path())
# 				assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/importRequestJobs'
# 				result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 				assert result is not None
# 				__reporter.store_response(name='test_post_import_request_jobs_{}_{}'.format(__id, time_stamp), data=result)


def test_file_transfer_location_post():
	time_stamp = __time_stamp.replace(':', '')
	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
	assert token == __token

	action = 'POST'
	assert action == 'POST'
	data = None
	assert data is None
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
	params = None
	assert params is None
	url = 'https://{0}'.format(__standard.file_transfer_location_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/fileTransferLocation'
	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	folder = __standard.gDirDataResponseFileTransferLocationPost
	__reporter.store_response(folder=folder, name='file_transfer_location_post_{}'.format(time_stamp), data=result)


# def test_bulk_load_external_events_post():
# 	time_stamp = __time_stamp.replace(':', '')
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	action = 'POST'
# 	assert action == 'POST'
# 	json_string = '''{
# 		"version": 1,
# 		"applicationId": ""
# 		}'''
# 	data = json.loads(json_string)
# 	data["applicationId"] = 'Identity Bridge Data'
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}'.format(__standard.bulk_load_external_events_path())
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingGateway/bulkEventsFileLocation'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
# 	folder = __standard.gDirDataResponseBulkLoadExternalEventsPost
# 	__reporter.store_response(folder=folder, name='bulk_load_external_events_post_{}'.format(time_stamp), data=result)


# def test_put_file_location_path():
# 	time_stamp = __time_stamp.replace(':', '')
# 	token = __security.generate_jwt(secret_key=__secret_key, tenant_id=__tenant_id)
# 	assert token == __token
#
# 	action = 'POST'
# 	assert action == 'POST'
# 	data = None
# 	assert data is None
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'}
# 	params = None
# 	assert params is None
# 	url = 'https://{0}'.format(__standard.file_transfer_location_path())
# 	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/fileTransferLocation'
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is not None
# 	__reporter.store_response(name='test_put_file_location_path_{}'.format(time_stamp), data=result)
#
# 	table_id = __standard.identity_bridge_table_id()
# 	assert table_id == __standard.identity_bridge_table_id()
#
# 	__signed_url = None
# 	if result is not None:
# 		__signed_url = result['signedURL']
# 		print('__signed_url = {0}'.format(__signed_url))
# 	temporary_url = __signed_url
# 	assert temporary_url is not None and temporary_url == __signed_url
#
# 	file_post_path = __standard.export_post_path()
# 	print('file_post_path = {0}'.format(file_post_path))
# 	assert file_post_path == 'D:/Clients/Example_Financial/SAS_CI360_Automation_Engine/data/test'
# 	file_export_path = __standard.export_path()
# 	file_export = '{0}_{1}{2}'.format(__standard.export_file()[:-4], time_stamp, '.CSV')
# 	print('file_export = {0}'.format(file_export))
# 	assert file_export == 'SASCHAIN_{}.CSV'.format(time_stamp)
# 	shutil.copy(Path('{0}/{1}'.format(file_post_path, __standard.export_file())), Path('{0}/{1}'.format(file_export_path, file_export)))
#
# 	action = 'PUT'
# 	assert action == 'PUT'
# 	data = '{0}/{1}'.format(file_export_path, file_export)
# 	print('data = {0}'.format(data))
# 	assert data == 'D:/Clients/Example_Financial/SAS_CI360_Automation_Engine/data/export/SASCHAIN_{}.CSV'.format(time_stamp)
# 	headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
# 	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json'}
# 	params = None
# 	assert params is None
# 	url = temporary_url
# 	assert url == __signed_url
# 	result = __connection.conn(action=action, data=data, headers=headers, params=params, url=url)
# 	assert result is None
