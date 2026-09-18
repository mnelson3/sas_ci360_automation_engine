#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from datetime import datetime

from connection import Connection
from security import Security
from standard import Standard

__prod_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6IjA1OTg2ODRhMDYwMDAxMGUyZWIyNDcxNCJ9.SPzyznE2MAdXOgXG7AIKr2ueWXJR5VcvTK5xlFf9cbQ'
__test_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6IjhhYTYxNmUzMzIwMDAxMGE1NjAwMTVmZCJ9.UMBKbVNyx2Z8jpAgpr6TfBvPWGpBKFwL8MMW9-E1O2k'
__dev_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'


def test_delete():
	pass


def test_get_mode():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	_mode = 'development'
	print('_mode : {0}'.format(_mode))

	connection = Connection.Connection()
	security = Security.Security()
	standard = Standard.Standard(mode=_mode)

	_secret_key = standard.secret_key_arr
	print('_secret_key : {0}'.format(_secret_key))
	_tenant_id = standard.tenant_id_arr
	print('_tenant_id : {0}'.format(_tenant_id))

	token = security.generate_jwt(secret_key=_secret_key, tenant_id=_tenant_id)
	assert token == __dev_token

	action = 'GET'
	assert action == 'GET'
	data = None
	assert data is None
	headers = {'Accept': 'application/vnd.sas.api+json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/vnd.sas.api+json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'}
	params = None
	assert params is None
	url = 'https://{0}{1}'.format(standard.external_gateway_path, standard.analytic_services_controller_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/analytic'
	result = connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	print('result : {0}'.format(result))


def test_get():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')

	standard = Standard.Standard()
	security = Security.Security()
	connection = Connection.Connection()

	_secret_key = standard.secret_key
	_tenant_id = standard.tenant_id

	token = security.generate_jwt(secret_key=_secret_key, tenant_id=_tenant_id)
	assert token == __dev_token

	action = 'GET'
	assert action == 'GET'
	data = None
	assert data is None
	headers = {'Accept': 'application/vnd.sas.api+json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/vnd.sas.api+json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'}
	params = None
	assert params is None
	url = 'https://{0}{1}'.format(standard.external_gateway_path, standard.analytic_services_controller_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/analytic'
	result = connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	print('result : {0}'.format(result))


def test_patch():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	pass


def test_post_mode():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	_mode = 'development'
	print('_mode : {0}'.format(_mode))

	connection = Connection.Connection()
	security = Security.Security()
	standard = Standard.Standard(mode=_mode)

	_secret_key = standard.secret_key
	_tenant_id = standard.tenant_id

	token = security.generate_jwt(secret_key=_secret_key, tenant_id=_tenant_id)
	assert token == __dev_token

	action = 'POST'
	assert action == 'POST'
	data = None
	assert data is None
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'}
	params = None
	assert params is None
	url = 'https://{0}{1}'.format(standard.external_gateway_path, standard.file_transfer_location_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/fileTransferLocation'
	result = connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	print('result : {0}'.format(result))


def test_post():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')

	standard = Standard.Standard()
	security = Security.Security()
	connection = Connection.Connection()

	_secret_key = standard.secret_key
	_tenant_id = standard.tenant_id

	token = security.generate_jwt(secret_key=_secret_key, tenant_id=_tenant_id)
	assert token == __dev_token

	action = 'POST'
	assert action == 'POST'
	data = None
	assert data is None
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(token)}
	assert headers == {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'}
	params = None
	assert params is None
	url = 'https://{0}{1}'.format(standard.external_gateway_path, standard.file_transfer_location_path)
	assert url == 'https://extapigwservice-training.ci360.sas.com/marketingData/fileTransferLocation'
	result = connection.conn(action=action, data=data, headers=headers, params=params, url=url)
	assert result is not None
	print('result : {0}'.format(result))


def test_put():
	_time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	pass
