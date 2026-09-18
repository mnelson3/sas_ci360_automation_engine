#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from custom import UploadIdentityBridgeData


def test_upload_identity_bridge_data_mode_development():
	mode = 'development'
	_custom = UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = _custom.run()
	print('result : {0}'.format(result))
	assert result is not None


def test_upload_identity_bridge_data_mode_test():
	mode = 'test'
	__custom = UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = __custom.run()
	print('result : {0}'.format(result))
	assert result is not None


def test_upload_identity_bridge_data_mode_production():
	mode = 'production'
	___custom = UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = ___custom.run()
	print('result : {0}'.format(result))
	assert result is not None


def test_upload_identity_bridge_data():
	____custom = UploadIdentityBridgeData.UploadIdentityBridgeData()
	result = ____custom.run()
	print('result : {0}'.format(result))
	assert result is not None
