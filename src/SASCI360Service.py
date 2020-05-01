#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import time
from logging.handlers import SysLogHandler
from pathlib import Path

from service import find_syslog, Service

from log import Log
from standard import Standard

_current_file_ = __file__
_real_path_ = os.path.realpath(_current_file_)
_dir_path_ = os.path.dirname(_real_path_)
_dir_name_ = os.path.basename(_dir_path_)
_src_path_ = os.path.abspath(os.path.join(_dir_path_, os.pardir))
_root_path_ = os.path.abspath(os.path.join(_src_path_, os.pardir))
sys.path.append(_dir_path_)
sys.path.append(Path(_dir_path_ + '/standard'))

_log_file_ = _src_path_ + Standard.gDirLog + 'service.log'
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class SASCI360Service(Service):

	def __init__(self, *args, **kwargs):
		super(SASCI360Service, self).__init__(*args, **kwargs)
		logger.addHandler(SysLogHandler(address=find_syslog(), facility=SysLogHandler.LOG_DAEMON))
		self.run()

	def restart(self):
		try:
			self.stop()
			self.start()
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None

	def run(self):
		try:
			src_path = Path(_dir_path_ + '/scheduler')
			sys.path.append(src_path)
			from scheduler import Scheduler
			s = Scheduler.Scheduler.get_instance()
			while not self.got_sigterm():
				s.run()
				time.sleep(60)
		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None


if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit('Syntax: %s COMMAND' % sys.argv[0])

	cmd = sys.argv[1].lower()
	service = SASCI360Service('SAS CI360 Automation Engine', pid_dir='/tmp')

	if cmd == 'start':
		service.start()
	elif cmd == 'stop':
		service.stop()
	elif cmd == 'restart':
		service.restart()
	elif cmd == 'status':
		if service.is_running():
			print("Service is running.")
		else:
			print("Service is not running.")
	else:
		sys.exit('Unknown command "%s".' % cmd)
