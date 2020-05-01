#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import datetime
from pathlib import Path

from custom import DownloadDiscover
from log import Log
from main import root_path
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'main.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Main:
    __instance = None

    @staticmethod
    def get_instance():
        if Main.__instance is None:
            Main()
        return Main.__instance

    def __init__(self):
        if Main.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            Main.__instance = self

        standard = Standard.Standard.get_instance()

        self._duration = standard.duration()
        self._end_date = standard.end_date()
        self._end_date_time = standard.end_date_time()
        self._end_time = standard.end_time()
        self._report_name = standard.report_name()
        self._start_date = standard.start_date()
        self._start_date_time = standard.start_date_time()
        self._start_time = standard.start_time()

    def run(self):
        try:
            duration = self._duration
            end_date = self._end_date
            end_date_time = self._end_date_time
            end_time = self._end_time
            report_name = self._report_name
            start_date = self._start_date
            start_date_time = self._start_date_time
            start_time = self._start_time

            if duration is None:
                duration = 24

            if end_date is None:
                end_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

            if end_date_time is None:
                end_date_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%dT%H:%M:%S.%fZ')

            if end_time is None:
                end_time = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S.%fZ')

            if start_date is None:
                start_date = datetime.datetime.strftime((datetime.datetime.now() - datetime.timedelta(hours=2)), '%Y-%m-%d')

            if start_date_time is None:
                start_date_time = datetime.datetime.strftime((datetime.datetime.now() - datetime.timedelta(hours=2)), '%Y-%m-%dT%H:%M:%S.%fZ')

            if start_time is None:
                start_time = datetime.datetime.strftime((datetime.datetime.now() - datetime.timedelta(hours=2)), '%H:%M:%S.%fZ')

            for item in report_name:
                if item != 'engage':
                    d = DownloadDiscover.Discover()
                    d.duration(duration)
                    d.end_date(end_date)
                    d.end_date_time(end_date_time)
                    d.end_time(end_time)
                    d.report_name(item)
                    d.start_date(start_date)
                    d.start_date_time(start_date_time)
                    d.start_time(start_time)
                    d.run()
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return


if __name__ == '__main__':
    Main.__init__(Main())
