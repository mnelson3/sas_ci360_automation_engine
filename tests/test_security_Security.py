#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from security import Security
from standard import Standard

__prod_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMyJ9.ZT31QADqh-vgFhGLAaTbPJiV3fmHqe8NZdnovNYD5-4'
__test_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMiJ9.4yCXGMeCm1aGTt66YLaYppUXnXpq2v6ZjnSSGC-V7s4'
__dev_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImExYTFhMWExYTFhMWExYTFhMWExYTEwMSJ9.q3MYDStIGHc7AGVHqyAXJuMojXHjO7uom_EipYB9vgo'


def test_generate_jwt_mode_development():
	mode = 'development'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'NbuOo1vj7C02NfJqFZ/t01Nroxw1O/hJ'
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'a1a1a1a1a1a1a1a1a1a1a101'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __dev_token


def test_generate_jwt_mode_test():
	mode = 'test'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == '0jtBp0UKuRYSSS4ClHxanzCmbuI2HURn'
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'a1a1a1a1a1a1a1a1a1a1a102'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __test_token


def test_generate_jwt_mode_production():
	mode = 'production'
	__security = Security.Security(mode=mode)
	__standard = Standard.Standard(mode=mode)
	secret_key = __standard.secret_key_arr
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'E0mExzZo7kjaNtCOBv6RjV9J79Gr8JYm'
	tenant_id = __standard.tenant_id_arr
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'a1a1a1a1a1a1a1a1a1a1a103'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __prod_token


def test_generate_jwt():
	__security = Security.Security()
	__standard = Standard.Standard()
	secret_key = __standard.secret_key
	print('secret_key : {0}'.format(secret_key))
	assert secret_key == 'NbuOo1vj7C02NfJqFZ/t01Nroxw1O/hJ'
	tenant_id = __standard.tenant_id
	print('tenant_id : {0}'.format(tenant_id))
	assert tenant_id == 'a1a1a1a1a1a1a1a1a1a1a101'
	result = __security.generate_jwt(tenant_id=tenant_id, secret_key=secret_key)
	print('result : {0}'.format(result))
	assert result == __dev_token
