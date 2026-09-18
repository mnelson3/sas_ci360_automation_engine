#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import time
from pathlib import Path

import requests

from connection import root_path
from log import Log

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'connection.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Connection:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Connection.__mode = kwargs['mode']
		else:
			Connection.__mode = None
		self.__mode = Connection.__mode

	@staticmethod
	def conn(result=None, **kwargs):
		try:
			response = None
			action = None
			data = None
			headers = None
			params = None
			url = None

			if 'action' in kwargs:
				action = kwargs['action']
			if 'data' in kwargs:
				data = kwargs['data']
			if 'headers' in kwargs:
				headers = kwargs['headers']
			if 'params' in kwargs:
				params = kwargs['params']
			if 'url' in kwargs:
				url = kwargs['url']

			code = 500
			counter = 0
			while (not 200 <= code <= 299) and (counter < 4):
				time.sleep(10)
				if action == 'DELETE':
					response = requests.delete(url=url, headers=headers)
				elif action == 'GET':
					response = requests.get(url=url, params=params, headers=headers)
				elif action == 'PATCH':
					response = requests.patch(url=url, data=data, headers=headers)
				elif action == 'POST':
					response = requests.post(url=url, data=data, headers=headers)
				elif action == 'PUT':
					response = requests.put(url=url, data=open(data, 'rb'), headers=headers)
				counter += 1
				code = int(response.status_code)
			if 200 <= code <= 299:
				if action == 'PUT':
					result = code
				else:
					result = response.json()
			else:
				result = response.text
			response.close()
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		return result


if __name__ == '__main__':
	Connection.__init__(Connection())
