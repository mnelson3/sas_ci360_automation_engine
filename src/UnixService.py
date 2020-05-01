#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import logging
import time
from logging.handlers import SysLogHandler

from service import find_syslog, Service


class UnixService(Service):
    def __init__(self, *args, **kwargs):
        super(UnixService, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(), facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)

    def run(self):
        while not self.got_sigterm():
            self.logger.info("I'm working...")
            time.sleep(5)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])

    cmd = sys.argv[1].lower()
    service = UnixService('SAS_CI360_Service', pid_dir='/tmp')

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
    elif cmd == 'status':
        if service.is_running():
            print("Service is running.")
        else:
            print("Service is not running.")
    else:
        sys.exit('Unknown command "%s".' % cmd)
