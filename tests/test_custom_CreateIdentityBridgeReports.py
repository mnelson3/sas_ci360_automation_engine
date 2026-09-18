#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from custom import CreateIdentityBridgeReports


def test_create_identity_bridge_reports_mode_development():
	mode = 'development'
	_custom = CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = _custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_create_identity_bridge_reports_mode_test():
	mode = 'test'
	__custom = CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = __custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_create_identity_bridge_reports_mode_production():
	mode = 'production'
	___custom = CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = ___custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_create_identity_bridge_reports():
	____custom = CreateIdentityBridgeReports.CreateIdentityBridgeReports()
	result = ____custom.run()
	print('result : {0}'.format(result))
	assert result is None
