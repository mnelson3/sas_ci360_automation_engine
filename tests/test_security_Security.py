#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from security import Security
from standard import Standard

__prod_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6IjA1OTg2ODRhMDYwMDAxMGUyZWIyNDcxNCJ9.eZw5gYkxdLe8FHbrS3ctcYOn4Z81mO32R2AdnvN8jHk'
__test_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6IjhhYTYxNmUzMzIwMDAxMGE1NjAwMTVmZCJ9.UMBKbVNyx2Z8jpAgpr6TfBvPWGpBKFwL8MMW9-E1O2k'
__dev_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJRCI6ImRkMGM3M2M5ZmUwMDAxM2M2MTc3NzJmOCJ9.10VFWYNCBjiu9EGGuRt9FojdrutkdYl-vTTgamSPfKc'


def test_generate_jwt_mode_development():
	mode = 'development'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'ODcxODE0bGkzaTNoMzM3MjdtZzJpMWpoY2M5ZTloaDY4'
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'dd0c73c9fe00013c617772f8'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __dev_token


def test_generate_jwt_mode_test():
	mode = 'test'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'MTkwNjEzMjNsN2w0a2FrbWVjZ2c2aGVrNzg4YWkzbTMxZzY='
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == '8aa616e33200010a560015fd'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __test_token


def test_generate_jwt_mode_production():
	mode = 'production'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'MjAwMTIxMTJoNGMxMWs2OTUwbWw2bGpkNmFpbmNuMDI0NTY='
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == '0598684a0600010e2eb24714'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __prod_token


def test_generate_jwt():
	__security = Security.Security()
	__standard = Standard.Standard()
	secret_key = __standard.secret_key
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'ODcxODE0bGkzaTNoMzM3MjdtZzJpMWpoY2M5ZTloaDY4'
	tenant_id = __standard.tenant_id
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'dd0c73c9fe00013c617772f8'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __dev_token
