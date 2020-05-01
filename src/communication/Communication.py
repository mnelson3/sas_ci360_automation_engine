#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from connection import root_path
from log import Log
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'communication.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class Communication:
    __instance = None

    @staticmethod
    def get_instance():
        if Communication.__instance is None:
            Communication()
        return Communication.__instance

    def __init__(self):
        if Communication.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            Communication.__instance = self

        standard = Standard.Standard.get_instance()

        self._email_server = standard.email_server()
        self._email_server_port = standard.email_server_port()
        self._email_server_login = standard.email_server_login()
        self._email_server_password = standard.email_server_password()

    def send_email(self, **kwargs):
        try:
            smtp = self._email_server
            port = self._email_server_port
            login = self._email_server_login
            password = self._email_server_password

            msg_from = kwargs['msg_from']
            msg_to = kwargs['msg_to']
            msg_subject = kwargs['msg_subject']
            # msg_file = kwargs['msg_file']

            # with open(msg_file, mode='rb') as message:
            # msg = MIMEText(message.read(), 'html', 'html')

            msg = MIMEMultipart()
            msg['From'] = msg_from
            msg['To'] = msg_to
            msg['Subject'] = msg_subject

            server = smtplib.SMTP(smtp, port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(login, password)
            server.send_message(msg)
            server.close()
        except Exception as e:
            logger.exception('Exception occurred: ' + str(e))
            return None
        finally:
            return


if __name__ == '__main__':
    Communication.__init__(Communication())
