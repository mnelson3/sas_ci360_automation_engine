#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from custom import SendIdentityBridgeSupportMessage


def test_send_identity_bridge_support_message_mode_development():
	mode = 'development'
	_custom = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = _custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_support_message_mode_test():
	mode = 'test'
	__custom = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = __custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_support_message_mode_production():
	mode = 'production'
	___custom = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = ___custom.run()
	print('result : {0}'.format(result))
	assert result is None


def test_send_identity_bridge_support_message():
	____custom = SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage()
	result = ____custom.run()
	print('result : {0}'.format(result))
	assert result is None
