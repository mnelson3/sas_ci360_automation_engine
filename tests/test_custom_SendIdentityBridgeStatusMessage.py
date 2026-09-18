#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from custom import SendIdentityBridgeStatusMessage


def test_send_identity_bridge_status_message_mode_development():
	mode = 'development'
	file_name = 'import_request_jobs_get_20200527160403'
	_custom = SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = _custom.run(file_name=file_name)
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_status_message_mode_test():
	mode = 'test'
	file_name = 'import_request_jobs_get_20200527160332'
	__custom = SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = __custom.run(file_name=file_name)
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_status_message_mode_production():
	mode = 'production'
	file_name = ''
	___custom = SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = ___custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_status_message():
	____custom = SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage()
	result = ____custom.run()
	print('result : {0}'.format(result))
	assert result is None
