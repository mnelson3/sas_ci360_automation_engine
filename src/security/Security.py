#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import base64
import json
from pathlib import Path

from jwt import JWT

from log import Log
from security import root_path
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'security.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Security:
	__instance = None

	@staticmethod
	def get_instance():
		if Security.__instance is None:
			Security()
		return Security.__instance

	def __init__(self):
		if Security.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			Security.__instance = self

		standard = Standard.Standard.get_instance()

		self._algorithm = standard.algorithm()
		self._encoding = standard.encoding()
		self._tenant_id = standard.tenant_id()

	def generate_jwt(self, result=None, **kwargs):
		try:
			algorithm = self._algorithm
			encoding = self._encoding
			tenant_id = self._tenant_id
			secret_key = kwargs['secret_key']
			payload = '{"clientID":"' + tenant_id + '"}'
			payload_json = json.loads(payload)
			secret_key_bytes = bytes(str(secret_key), encoding=encoding)
			secret_key_encoded = base64.b64encode(secret_key_bytes)
			result = JWT.encode(payload_json, secret_key_encoded, algorithm)
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None
		finally:
			return result


if __name__ == '__main__':
	Security.__init__(Security())
