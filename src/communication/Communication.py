#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from communication import root_path
from log import Log
from standard import Standard

__log_file = Path('{0}{1}{2}'.format(root_path, '/logs/', 'communication.log'))
__log = Log.Log.get_instance()
__log.log_file(__log_file)
logger = __log.logging()


class Communication:
	__mode = None

	def __init__(self, **kwargs):
		if 'mode' in kwargs:
			Communication.__mode = kwargs['mode']
		else:
			Communication.__mode = None
		self.__mode = Communication.__mode

		if self.__mode is not None:
			self._standard = Standard.Standard(mode=self.__mode)
			self._email_server = self._standard.email_server_arr
			self._email_server_login = self._standard.email_server_login_arr
			self._email_server_password = self._standard.email_server_password_arr
			self._email_server_port = self._standard.email_server_port_arr
		else:
			self._standard = Standard.Standard()
			self._email_server = self._standard.email_server
			self._email_server_login = self._standard.email_server_login
			self._email_server_password = self._standard.email_server_password
			self._email_server_port = self._standard.email_server_port

	@property
	def email_server(self):
		try:
			return self._email_server
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_login(self):
		try:
			return self._email_server_login
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_password(self):
		try:
			return self._email_server_password
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	@property
	def email_server_port(self):
		try:
			return int(self._email_server_port)
		except AttributeError or Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None

	def send_email(self, result=None, **kwargs):
		try:
			email_msg_from = None
			email_msg_to = None
			email_msg_cc = None
			email_msg_bcc = None
			email_msg_subject = None
			email_msg_body = None
			email_msg_attachment = None

			host = self.email_server
			port = self.email_server_port
			login = self.email_server_login
			password = self.email_server_password

			if 'email_msg_from' in kwargs:
				email_msg_from = kwargs['email_msg_from']
			if 'email_msg_to' in kwargs:
				email_msg_to = kwargs['email_msg_to']
			if 'email_msg_cc' in kwargs:
				email_msg_cc = kwargs['email_msg_cc']
			if 'email_msg_bcc' in kwargs:
				email_msg_bcc = kwargs['email_msg_bcc']
			if 'email_msg_subject' in kwargs:
				email_msg_subject = kwargs['email_msg_subject']
			if 'email_msg_body' in kwargs:
				email_msg_body = kwargs['email_msg_body']
			if 'email_msg_attachment' in kwargs:
				email_msg_attachment = kwargs['email_msg_attachment']

			message = MIMEMultipart()
			message['From'] = email_msg_from
			message['To'] = email_msg_to
			message['CC'] = email_msg_cc
			message['BCC'] = email_msg_bcc
			message['Subject'] = email_msg_subject

			# Add body to email
			message.attach(MIMEText(email_msg_body, "plain"))

			if email_msg_attachment is not None:
				filename = email_msg_attachment

				# Open PDF file in binary mode
				with open(filename, "rb") as attachment:
					# Add file as application/octet-stream
					# Email client can usually download this automatically as attachment
					part = MIMEBase("application", "octet-stream")
					part.set_payload(attachment.read())

				# Encode file in ASCII characters to send by email
				encoders.encode_base64(part)

				# Add header as key/value pair to attachment part
				part.add_header(
					"Content-Disposition",
					f"attachment; filename= {filename}",
				)

				# Add attachment to message and convert message to string
				message.attach(part)

			text = message.as_string()
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
				server.login(login, password)
				server.sendmail(email_msg_from, email_msg_to, text)
			server.close()
		except Exception as e:
			logger.exception('Exception occurred: {}'.format(str(e)))
			return None
		finally:
			return result


if __name__ == '__main__':
	Communication.__init__(Communication())
