#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import codecs
import csv
import os
from pathlib import Path

from custom import root_path
from log import Log
from standard import Standard

import ftfy

_log_file_ = Path(root_path + Standard.gDirLog + 'standard-clean_data.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class CleanData:
    __instance = None

    @staticmethod
    def get_instance():
        if CleanData.__instance is None:
            CleanData()
        return CleanData.__instance

    def __init__(self, **kwargs):
        if CleanData.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            CleanData.__instance = self

        if 'report_date' in kwargs:
            self._report_date = kwargs['report_date']

    def report_date(self, value=None):
        if value:
            self._report_date = value
        try:
            return self._report_date
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    @staticmethod
    def clean_control_data(self):
        try:
            report_date = self.report_date()
            path = Path(root_path + Standard.gDsDscCsv)
            for filename in os.listdir(path=path):
                file_name = os.path.splitext(filename)[0]
                file_path = path.joinpath(filename)
                table_name = str(file_name) + '_' + str(report_date) + '.csv'
                out_path = Path(root_path + Standard.gDsDscFix + table_name)
                csv.register_dialect('sas', delimiter='|', lineterminator='\r\n', escapechar='\\', quoting=csv.QUOTE_NONE)
                with open(file=file_path, mode='r', newline='', encoding='UTF-8', errors='replace') as in_file, open(file=out_path, mode='w', newline='', encoding='UTF-8', errors='replace') as out_file:
                    csv_reader = csv.reader(in_file, dialect='sas')
                    csv_writer = csv.writer(out_file, dialect='sas')
                    for row in csv_reader:
                        for i in range(len(row)):
                            ftfy.fix_text(i, '*', fix_entities='auto', remove_terminal_escapes=True, fix_encoding=True, fix_latin_ligatures=True, fix_character_width=True, uncurl_quotes=True, fix_line_breaks=True, fix_surrogates=True, remove_control_chars=True, remove_bom=True, normalization='NFC', max_decode_length=1000000)
                            row[i] = ftfy.fix_text(row[i], fix_entities=True, fix_encoding=True, uncurl_quotes=True, fix_latin_ligatures=True, fix_character_width=True, fix_surrogates=True, remove_control_chars=True, normalization='NKFC')
                            row[i] = ftfy.fix_text(row[i])
                        csv_writer.writerow(row)
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return

    @staticmethod
    def clean_foreign_data():
        try:
            path = Path(root_path + Standard.gDsDscFix)
            for filename in os.listdir(path=path):
                file_name = os.path.splitext(filename)[0]
                file_path = path.joinpath(filename)
                table_name = str(file_name) + '.csv'
                out_path = Path(root_path + Standard.gDsDscClean + table_name)
                csv.register_dialect('sas', delimiter='|', lineterminator='\r\n', escapechar='\\', quoting=csv.QUOTE_NONE)
                with codecs.open(filename=file_path, mode='r', encoding='UTF-8', errors='replace') as in_file, codecs.open(filename=out_path, mode='w', encoding='UTF-8', errors='replace') as out_file:
                    csv_reader = csv.reader(in_file, dialect='sas')
                    csv_writer = csv.writer(out_file, dialect='sas')
                    for row in csv_reader:
                        for i in range(len(row)):
                            for c in range(len(row[i])):
                                try:
                                    if ord(row[i][c]) > 256:
                                        row[i] = str(row[i]).replace(row[i][c], '?')
                                except (IndexError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError):
                                    row[i] = str(row[i]).replace(row[i][c], '?')
                        csv_writer.writerow(row)
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return

    def run(self):
        try:
            self.clean_control_data(self)
            self.clean_foreign_data()
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return


if __name__ == '__main__':
    CleanData.__init__(CleanData())
