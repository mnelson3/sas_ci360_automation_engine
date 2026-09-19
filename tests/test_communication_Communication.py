#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from communication import Communication
from standard import Standard

__email_msg_status_from = 'example.sender@example.com'
__email_msg_status_to = 'example.recipient@example.com'
__email_msg_support_from = 'example.sender@example.com'
__email_msg_support_to = 'example.recipient@example.com'
__email_msg_support_cc = 'example.recipient@example.com'
__email_server = 'smtp.gmail.com'
__email_server_login = 'example.sender@example.com'
__email_server_password = 'Ex4mpl3-P@ss'
__email_server_port = 465


def test_standard_settings_mode():
	mode = 'development'
	print('mode : {0}'.format(mode))

	standard = Standard.Standard(mode=mode)
	assert standard.email_msg_status_from_arr == __email_msg_status_from
	assert standard.email_msg_status_to_arr == __email_msg_status_to
	assert standard.email_msg_support_from_arr == __email_msg_support_from
	assert standard.email_msg_support_to_arr == __email_msg_support_to
	assert standard.email_msg_support_cc_arr == __email_msg_support_cc


def test_standard_settings():
	standard = Standard.Standard()
	assert standard.email_msg_status_from == __email_msg_status_from
	assert standard.email_msg_status_to == __email_msg_status_to
	assert standard.email_msg_support_from == __email_msg_support_from
	assert standard.email_msg_support_to == __email_msg_support_to
	assert standard.email_msg_support_cc == __email_msg_support_cc


def test_communication_settings_mode():
	mode = 'development'
	print('mode : {0}'.format(mode))

	communication = Communication.Communication(mode=mode)
	assert communication.email_server == __email_server
	assert communication.email_server_login == __email_server_login
	assert communication.email_server_password == __email_server_password
	assert communication.email_server_port == __email_server_port


def test_communication_settings():
	communication = Communication.Communication()
	assert communication.email_server == __email_server
	assert communication.email_server_login == __email_server_login
	assert communication.email_server_password == __email_server_password
	assert communication.email_server_port == __email_server_port


def test_communication_send_status_message_mode():
	mode = 'development'
	print('mode : {0}'.format(mode))
	time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	time_stamp_ = '20200519120935'

	communication = Communication.Communication(mode=mode)
	standard = Standard.Standard(mode=mode)

	email_msg_status_from = standard.email_msg_status_from_arr
	email_msg_status_to = standard.email_msg_status_to_arr
	report_folder = standard.reports_path_arr

	file_name = 'import_request_jobs_get_{}'.format(time_stamp_)
	csv_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', report_folder, file_name, '.CSV'))

	email_msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY] <{}>'.format(email_msg_status_from)
	email_msg_to = email_msg_status_to
	email_msg_subject = 'Daily Identity Bridge Update [{0}]'.format(time_stamp)
	email_msg_body = ''
	email_msg_attachment = csv_file

	result = communication.send_email(
		email_msg_from=email_msg_from,
		email_msg_to=email_msg_to,
		email_msg_subject=email_msg_subject,
		email_msg_body=email_msg_body,
		email_msg_attachment=email_msg_attachment
	)
	assert result is None


def test_communication_send_status_message():
	time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	time_stamp_ = '20200519120935'

	communication = Communication.Communication()
	standard = Standard.Standard()

	email_msg_status_from = standard.email_msg_status_from
	email_msg_status_to = standard.email_msg_status_to
	report_folder = standard.reports_path

	file_name = 'import_request_jobs_get_{}'.format(time_stamp_)
	csv_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', report_folder, file_name, '.CSV'))

	email_msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY] <{}>'.format(email_msg_status_from)
	email_msg_to = email_msg_status_to
	email_msg_subject = 'Daily Identity Bridge Update [{0}]'.format(time_stamp)
	email_msg_body = ''
	email_msg_attachment = csv_file

	result = communication.send_email(
		email_msg_from=email_msg_from,
		email_msg_to=email_msg_to,
		email_msg_subject=email_msg_subject,
		email_msg_body=email_msg_body,
		email_msg_attachment=email_msg_attachment
	)
	assert result is None


def test_communication_send_support_message_mode():
	mode = 'development'
	print('mode : {0}'.format(mode))
	time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	time_stamp_ = '20200519120935'

	communication = Communication.Communication(mode=mode)
	standard = Standard.Standard(mode=mode)

	email_msg_support_from = standard.email_msg_support_from_arr
	email_msg_support_to = standard.email_msg_support_to_arr
	email_msg_support_cc = standard.email_msg_support_cc_arr
	export_folder = standard.export_path_arr

	file_name = 'SASCHANGE_{}'.format(time_stamp_)
	csv_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', export_folder, file_name, '.CSV'))

	tenant_environment = standard.tenant_environment_arr
	tenant_name = standard.tenant_name_arr
	tenant_number = standard.tenant_number_arr
	tenant_product = standard.tenant_product_arr
	tenant_url = standard.tenant_url_arr

	email_msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY] <{}>'.format(email_msg_support_from)
	email_msg_to = email_msg_support_to
	email_msg_cc = email_msg_support_cc
	email_msg_subject = 'Identity Bridge Change Update [{0}]'.format(time_stamp)
	email_msg_body = 'Environment: {0}\n' \
	    'Name: {1}\n' \
	    'Number: {2}\n' \
	    'Product: {3}\n' \
	    'URL: {4}\n' \
	    'User: {5}\n' \
	    'Time of attempt: {6}\n' \
	    'Issue:'.format(tenant_environment, tenant_name, tenant_number, tenant_product, tenant_url, email_msg_from, time_stamp)
	email_msg_attachment = csv_file

	result = communication.send_email(
		email_msg_from=email_msg_from,
		email_msg_to=email_msg_to,
		email_msg_cc=email_msg_cc,
		email_msg_subject=email_msg_subject,
		email_msg_body=email_msg_body,
		email_msg_attachment=email_msg_attachment
	)
	assert result is None


def test_communication_send_support_message():
	time_stamp = datetime.now().strftime('%Y:%m:%d:%H:%M:%S')
	time_stamp_ = '20200519120935'

	communication = Communication.Communication()
	standard = Standard.Standard()

	tenant_environment = standard.tenant_environment
	tenant_name = standard.tenant_name
	tenant_number = standard.tenant_number
	tenant_product = standard.tenant_product
	tenant_url = standard.tenant_url

	email_msg_support_from = standard.email_msg_status_from
	email_msg_support_to = standard.email_msg_status_to
	email_msg_support_cc = standard.email_msg_support_cc
	export_folder = standard.export_path_arr

	file_name = 'SASCHANGE_{}'.format(time_stamp_)
	csv_file = Path('{0}{1}{2}{3}'.format('D:\Clients\Example_Financial\SAS_CI360_Automation_Engine', export_folder, file_name, '.CSV'))

	email_msg_from = 'SAS CI360 Automation Engine [DO-NOT-REPLY] <{}>'.format(email_msg_support_from)
	email_msg_to = email_msg_support_to
	email_msg_cc = email_msg_support_cc
	email_msg_subject = 'Identity Bridge Change Update [{0}]'.format(time_stamp)
	email_msg_body = 'Environment: {0}\n' \
	    'Name: {1}\n' \
	    'Number: {2}\n' \
	    'Product: {3}\n' \
	    'URL: {4}\n' \
	    'User: {5}\n' \
	    'Time of attempt: {6}\n' \
	    'Issue:'.format(tenant_environment, tenant_name, tenant_number, tenant_product, tenant_url, email_msg_from, time_stamp)
	email_msg_attachment = csv_file

	result = communication.send_email(
		email_msg_from=email_msg_from,
		email_msg_to=email_msg_to,
		email_msg_cc=email_msg_cc,
		email_msg_subject=email_msg_subject,
		email_msg_body=email_msg_body,
		email_msg_attachment=email_msg_attachment
	)
	assert result is None
