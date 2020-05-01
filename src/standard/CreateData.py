#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import json
import os
from pathlib import Path

import requests

from standard import root_path
from log import Log
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'standard-create_data.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class CreateData:
    __instance = None

    @staticmethod
    def get_instance():
        if CreateData.__instance is None:
            CreateData()
        return CreateData.__instance

    def __init__(self, **kwargs):
        if CreateData.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            CreateData.__instance = self

        standard = Standard.Standard.get_instance()

        self._flag_csv_header = standard.flag_csv_header()
        self._delimiter = standard.delimiter()

        if 'entity' in kwargs:
            self._entity = kwargs['entity']
        if 'header' in kwargs:
            self._header = kwargs['header']
        if 'in_delimiter' in kwargs:
            self._in_delimiter = kwargs['in_delimiter']
        if 'in_file' in kwargs:
            self._in_file = kwargs['in_file']
        if 'out_delimiter' in kwargs:
            self._out_delimiter = kwargs['out_delimiter']
        if 'out_file' in kwargs:
            self._out_file = kwargs['out_file']
        if 'report_date' in kwargs:
            self._report_date = kwargs['report_date']
        if 'schema_url' in kwargs:
            self._schema_url = kwargs['schema_url']

    def entity(self, value=None):
        if value:
            self._entity = value
        try:
            return self._entity
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def header(self, value=None):
        if value:
            self._header = value
        try:
            return self._header
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def in_delimiter(self, value=None):
        if value:
            self._in_delimiter = value
        try:
            return self._in_delimiter
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def in_file(self, value=None):
        if value:
            self._in_file = value
        try:
            return self._in_file
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def out_delimiter(self, value=None):
        if value:
            self._out_delimiter = value
        try:
            return self._out_delimiter
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def out_file(self, value=None):
        if value:
            self._out_file = value
        try:
            return self._out_file
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def report_date(self, value=None):
        if value:
            self._report_date = value
        try:
            return self._report_date
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def schema_url(self, value=None):
        if value:
            self._schema_url = value
        try:
            return self._schema_url
        except AttributeError or Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None

    def create_csv(self):
        try:
            in_delimiter = Standard.gSohDelimiter
            flag_csv_header = self._flag_csv_header
            in_file = self.in_file()
            header = self.header()
            out_delimiter = self._delimiter
            out_file = self.out_file()
            with open(file=str(in_file), mode='r', encoding='UTF-8') as in_f, open(file=str(out_file), mode='a', encoding='UTF-8') as out_f:
                if flag_csv_header is True:
                    out_f.write(str(header) + '\n')
                rows = 0
                for line in in_f:
                    rows = rows + 1
                    try:
                        line = line.replace('|', '-').replace(str(in_delimiter), str(out_delimiter))
                        out_f.write(line + '\n')
                    except AttributeError or Exception as e:
                        logger.exception('Exception occurred: ' + str(e))
                        return None
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return

    def append_csv(self):
        try:
            in_delimiter = Standard.gSohDelimiter
            in_file = self.in_file()
            out_delimiter = self._delimiter
            out_file = self.out_file()
            with open(file=str(in_file), mode='r', encoding='UTF-8') as in_f, open(file=str(out_file), mode='a', encoding='UTF-8') as out_f:
                rows = 0
                for line in in_f:
                    rows = rows + 1
                    try:
                        line = line.replace('|', '-').replace(str(in_delimiter), str(out_delimiter))
                        out_f.write(line + '\n')
                    except AttributeError or Exception as e:
                        logger.exception('Exception occurred: ' + str(e))
                        return None
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return

    def create_single_table_files(self):
        try:
            delimiter = self._delimiter
            entity = self.entity()
            schema_url = self.schema_url()
            name = entity['entityName']
            table_file = Path(root_path + Standard.gDsDscCsv + name + '.csv')
            if not os.path.exists(table_file):
                header = self.get_schema(entity=name, schema_url=schema_url, delimiter=delimiter)
                with open(file=table_file, mode='w', encoding='UTF-8') as f:
                    f.write(header + '\n')
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return

    @staticmethod
    def get_schema(entity, schema_url, delimiter):
        column_header = ''
        sql_column = ''
        sql_insert_column = ''
        try:
            table_name = entity
            url = schema_url
            delimiter = delimiter
            response = requests.get(url=url).text.encode(encoding='UTF-8', errors='replace')
            json_meta = json.loads(response)
            sql_table = 'create table ' + table_name + '('
            sql_insert = 'insert into ' + table_name + ' values ('
            for item in json_meta:
                meta_table = item['table_name']
                if table_name.lower() == meta_table.lower():
                    column = str(item['column_name'])
                    column_type = str(item['column_type'])
                    sql_column = sql_column + '\n  ' + column + ' ' + column_type + ', '
                    sql_insert_column = sql_insert_column + '%s,'
                    column_header = column_header + column + delimiter
            Standard.gSql += sql_table + sql_column[:-2] + ');\n\n'
            Standard.gSqlInsert = sql_insert + sql_insert_column[:-1] + ')'
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            # remove last delimiter and return line
            return column_header[:-len(delimiter)]


if __name__ == '__main__':
    CreateData.__init__(CreateData())
