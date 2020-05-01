#! /venv/bin/python
# -*- mode: python ; coding: utf-8 -*-

import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas

from custom import root_path
from log import Log
from standard import Standard

_log_file_ = Path(root_path + Standard.gDirLog + 'custom-build_email_data.log')
_log_ = Log.Log.get_instance()
_log_.log_file(_log_file_)
logger = _log_.logging()


class BuildEmailData:
	__instance = None

	@staticmethod
	def get_instance():
		if BuildEmailData.__instance is None:
			BuildEmailData()
		return BuildEmailData.__instance

	def __init__(self):
		if BuildEmailData.__instance is not None:
			raise Exception('This class is a singleton!')
		else:
			BuildEmailData.__instance = self

		standard = Standard.Standard.get_instance()

		self._export_prod_path = standard.export_prod_path()
		self._export_test_path = standard.export_test_path()
		self._export_prod_file = standard.export_prod_file()
		self._export_test_file = standard.export_test_file()
		self._flag_test_export = standard.flag_test_export()
		self._flag_test_report = standard.flag_test_report()
		self._suppression_email_domain_list = standard.suppression_email_domain_list()
		self._suppression_form_name_list = standard.suppression_form_name_list()

	def build_email_list(self):
		try:
			flag_test_export = self._flag_test_export
			flag_test_report = self._flag_test_report

			if flag_test_export is True:
				customer_datamart = Path(self._export_test_path + 'identity_bridge_data.csv')
			else:
				customer_datamart = Path(self._export_prod_path + 'identity_bridge_data.csv')

			customer_datamart_dataframe = pandas.read_csv(filepath_or_buffer=customer_datamart, sep=',', delimiter=',', encoding='UTF-8')
			suppression_email_domain_list = self._suppression_email_domain_list
			# suppression_form_name_list = self.suppression_form_name_list()

			today = pandas.to_datetime(datetime.now())
			current_hour_datetime = today.floor('H').to_pydatetime()
			suppression_hour = today + timedelta(hours=-1)
			suppression_hour_datetime = suppression_hour.floor('H').to_pydatetime()
			target_hour = today + timedelta(hours=-2)
			target_hour_datetime = target_hour.floor('H').to_pydatetime()
			path = Path(root_path + Standard.gDsDscClean)
			folder = str(datetime.now()).replace(' ', '_').replace(':', '_').replace('-', '_').replace('.', '_')

			if flag_test_export is True and flag_test_report is True:
				path_out = Path(Standard.gCustomerDataMartProd + '/' + folder + '/')
				os.makedirs(path_out)
			elif flag_test_export is True and flag_test_report is False:
				path_out = Path(root_path + Standard.gDsDscExport + Standard.gDsDscExportTestFile)
			else:
				path_out = Path(root_path + Standard.gDsDscExport + Standard.gDsDscExportProdFile)

			page_details_dataframe = pandas.DataFrame()
			form_details_dataframe = pandas.DataFrame()

			for filename in os.listdir(path=path):
				if str(filename).startswith('PAGE_DETAILS') and not str(filename).startswith('PAGE_DETAILS_EXT'):
					file_path = path.joinpath(filename)
					page_details_dataframe = pandas.read_csv(filepath_or_buffer=file_path, sep='|', delimiter='|', encoding='UTF-8')
				if str(filename).startswith('FORM_DETAILS'):
					file_path = path.joinpath(filename)
					form_details_dataframe = pandas.read_csv(filepath_or_buffer=file_path, sep='|', delimiter='|', encoding='UTF-8')

			if flag_test_export is True and flag_test_report is True:
				page_details_dataframe.to_csv(path_or_buf=path_out.joinpath('page_details_dataframe.csv'), sep=',', index=False, header=False)
				form_details_dataframe.to_csv(path_or_buf=path_out.joinpath('form_details_dataframe.csv'), sep=',', index=False, header=False)

			target_page_details_dataframe = page_details_dataframe
			suppression_page_details_dataframe = page_details_dataframe
			target_form_details_dataframe = form_details_dataframe
			suppression_form_details_dataframe = form_details_dataframe

			target_page_details_df = (
				target_page_details_dataframe[
					(target_page_details_dataframe['detail_dttm_tz'] > str(target_hour_datetime))
					& (target_page_details_dataframe['detail_dttm_tz'] <= str(suppression_hour_datetime))
					& (target_page_details_dataframe['domain_nm'] == 'support.worldwildlife.org')
					]
			)

			if flag_test_export is True and flag_test_report is True:
				target_page_details_df.to_csv(path_or_buf=path_out.joinpath('target_page_details_df.csv'), sep=',', index=False, header=False)

			target_form_details_df = (
				target_form_details_dataframe[
					(target_form_details_dataframe.detail_id.isin(target_page_details_df.detail_id))
					& (target_form_details_dataframe.identity_id.isin(target_page_details_df.identity_id))
					& (target_form_details_dataframe['form_field_detail_dttm_tz'] > str(target_hour_datetime))
					& (target_form_details_dataframe['form_field_detail_dttm_tz'] <= str(suppression_hour_datetime))
					& (target_form_details_dataframe['attempt_status_cd'] == '0_Not Submitted')
					]
			)

			if flag_test_export is True and flag_test_report is True:
				target_form_details_df.to_csv(path_or_buf=path_out.joinpath('target_form_details_df.csv'), sep=',', index=False, header=False)

			suppression_page_details_df = (
				suppression_page_details_dataframe[
					(suppression_page_details_dataframe['detail_dttm_tz'] > str(suppression_hour_datetime))
					& (suppression_page_details_dataframe['detail_dttm_tz'] <= str(current_hour_datetime))
					& (suppression_page_details_dataframe['domain_nm'] == 'support.worldwildlife.org')
					]
			)

			if flag_test_export is True and flag_test_report is True:
				suppression_page_details_df.to_csv(path_or_buf=path_out.joinpath('suppression_page_details_df.csv'), sep=',', index=False, header=False)

			suppression_form_details_df = (
				suppression_form_details_dataframe[
					(~suppression_form_details_dataframe.detail_id.isin(suppression_page_details_df.detail_id))
					& (~suppression_form_details_dataframe.identity_id.isin(suppression_page_details_df.identity_id))
					& (suppression_form_details_dataframe['form_field_detail_dttm_tz'] > str(suppression_hour_datetime))
					& (suppression_form_details_dataframe['form_field_detail_dttm_tz'] <= str(current_hour_datetime))
					& (suppression_form_details_dataframe['attempt_status_cd'] == '3_Submitted Successfully')
					]
			)

			if flag_test_export is True and flag_test_report is True:
				suppression_form_details_df.to_csv(path_or_buf=path_out.joinpath('suppression_form_details_df.csv'), sep=',', index=False, header=False)

			target_df = (
				target_form_details_df[
					(~target_form_details_df.identity_id.isin(suppression_form_details_df.identity_id))
				]
			)

			if flag_test_export is True and flag_test_report is True:
				target_df.to_csv(path_or_buf=path_out.joinpath('target_df.csv'), sep=',', index=False, header=False)

			suppression_df_is_valid_email = (
				target_df[
					(target_df.identity_id.isin(customer_datamart_dataframe.identity_id))
				]
			)

			if flag_test_export is True and flag_test_report is True:
				suppression_df_is_valid_email.to_csv(path_or_buf=path_out.joinpath('suppression_df_is_valid_email.csv'), sep=',', index=False, header=False)

			result_dataframe = (
				suppression_df_is_valid_email[
					(~suppression_df_is_valid_email.email.isin(suppression_email_domain_list))
				]
			)

			if flag_test_export is True and flag_test_report is True:
				result_dataframe.to_csv(path_or_buf=path_out.joinpath('result_dataframe.csv'), sep=',', index=False, header=False)

			if flag_test_report is True:
				result_dataframe = result_dataframe[['identity_id', 'email', 'form_field_detail_dttm_tz']]
			else:
				result_dataframe = result_dataframe[['identity_id', 'email']]

			result_out_dataframe = result_dataframe
			result_out_dataframe.insert(0, 'eventName', 'CART_Email_Event')
			result_out_dataframe.insert(1, 'entityName', 'visitor_id')
			result_out_dataframe.insert(2, 'entityValue', result_dataframe['identity_id'])
			result_out_dataframe.insert(3, 'attrName1', 'taskName')
			result_out_dataframe.insert(4, 'attrValue1', 'CART_Donations_Triggered_Email')
			result_out_dataframe.insert(5, 'attrName2', 'emailAddress')
			result_out_dataframe.insert(6, 'attrValue2', result_dataframe['email'])
			if flag_test_export is True and flag_test_report is True:
				result_out_dataframe.insert(7, 'attrName3', 'form_field_detail_dttm_tz')
				result_out_dataframe.insert(8, 'attrValue3', result_dataframe['form_field_detail_dttm_tz'])
			if flag_test_export is True and flag_test_report is True:
				result_out_dataframe = result_out_dataframe.drop(columns=['identity_id', 'email', 'form_field_detail_dttm_tz'])
			else:
				result_out_dataframe = result_out_dataframe.drop(columns=['identity_id', 'email'])
			result_out_dataframe.to_csv(path_or_buf=path_out, sep=',', index=False, header=False)

			flag_test_export = self._flag_test_export
			logger.info(msg=flag_test_export)

			if flag_test_export is True:
				email_list = Path(root_path + self._export_test_path + self._export_test_file)
			else:
				email_list = Path(root_path + self._export_prod_path + self._export_prod_file)
			logger.info(msg=email_list)

			response = post_bulk_load_external_events
			url_put = kwargs['url_put']
			json_post = kwargs['json_post']
			for items in json_post['links']:
				url_put = items['href']
			result = self.put_file_location(self, result, json_post=json_post)

		except Exception as e:
			logger.exception('Exception occurred: ' + str(e))
			return None
		finally:
			return


if __name__ == '__main__':
	BuildEmailData.__init__(BuildEmailData())
