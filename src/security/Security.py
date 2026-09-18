#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import base64
from pathlib import Path

import jwt

from security import root_path
from log import Log
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'security.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Security:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Security.__mode = kwargs['mode']
		else:
			Security.__mode = None
		self.__mode = Security.__mode

		if self.__mode is not None:
			self._standard = Standard.Standard(mode=self.__mode)
		else:
			self._standard = Standard.Standard()

		self._algorithm = self._standard.algorithm
		self._encoding = self._standard.encoding

	def generate_jwt(self, result=None, **kwargs):
		try:
			algorithm = self._algorithm
			encoding = self._encoding

			tenant_id = kwargs['tenant_id']
			secret_key = kwargs['secret_key']

			payload = {'clientID': '{0}'.format(tenant_id)}
			secret_key_bytes = bytes(str(secret_key), encoding=encoding)
			secret_key_encoded = base64.b64encode(secret_key_bytes)
			token = jwt.encode(payload=payload, key=secret_key_encoded, algorithm=algorithm)
			result = token.decode()
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return result


if __name__ == '__main__':
	Security.__init__(Security())
