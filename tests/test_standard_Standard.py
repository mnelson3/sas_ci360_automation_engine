#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from standard import Standard

__standard = Standard.Standard()


def test_globals():
	assert __standard.gSql == ''
	assert __standard.gSqlInsert == ''
	assert __standard.gQuerystring == {}
	assert __standard.gSohDelimiter == '\001'
	assert __standard.gDirRoot == '/SAS_CI360_Automation_Engine/'
	assert __standard.gDirConfig == '/config/'
	assert __standard.gDirLog == '/logs/'
	assert __standard.gDirData == '/data/'
	assert __standard.gDirDataResponse == '/data/response/'
	assert __standard.gDirDataResponseAnalyticGet == '/data/response/analytic_get/'
	assert __standard.gDirDataResponseAnalyticPost == '/data/response/analytic_post/'
	assert __standard.gDirDataResponseAnalyticTransfersPost == '/data/response/analytic_transfers_post/'
	assert __standard.gDirDataResponseCustomerJobsGet == '/data/response/customer_jobs_get/'
	assert __standard.gDirDataResponseCustomerJobsPost == '/data/response/customer_jobs_post/'
	assert __standard.gDirDataResponseEventJobsGet == '/data/response/event_jobs_get/'
	assert __standard.gDirDataResponseEventJobsPost == '/data/response/event_jobs_post/'
	assert __standard.gDirDataResponseExportRequestJobsGet == '/data/response/export_request_jobs_get/'
	assert __standard.gDirDataResponseExportRequestJobsPost == '/data/response/export_request_jobs_post/'
	assert __standard.gDirDataResponseIdentityRecordsGet == '/data/response/identity_records_get/'
	assert __standard.gDirDataResponseImportRequestJobsGet == '/data/response/import_request_jobs_get/'
	assert __standard.gDirDataResponseImportRequestJobsPost == '/data/response/import_request_jobs_post/'
	assert __standard.gDirDataResponseTablesGet == '/data/response/tables_get/'
	assert __standard.gDirDataResponseTablesPost == '/data/response/tables_post/'
	assert __standard.gDsDscRoot == '/data/discover/'
	assert __standard.gDsDscClean == '/data/discover/clean/'
	assert __standard.gDsDscConfig == '/data/discover/dsccnfg/'
	assert __standard.gDsDscZip == '/data/discover/dscdonl/'
	assert __standard.gDsDscExtr == '/data/discover/dscextr/'
	assert __standard.gDsDscCsv == '/data/discover/dscwh/'
	assert __standard.gDsDscExport == '/data/discover/export/'
	assert __standard.gDsDscFix == '/data/discover/fix/'
	assert __standard.gDsDscSql == '/data/discover/sql/'
	assert __standard.gDsEngRoot == '/data/engage/'
	assert __standard.gDsEngDownload == '/data/engage/download/'
	assert __standard.gDsEngExport == '/data/engage/export/'
	assert __standard.gDsEngJson == '/data/engage/json/'
	assert __standard.gDsEngProcessA == '/data/engage/process_a/'
	assert __standard.gDsEngProcessB == '/data/engage/process_b/'
	assert __standard.gDsEngProcessC == '/data/engage/process_c/'
	assert __standard.gDsEngProcessD == '/data/engage/process_d/'
	assert __standard.gDsEngProcessE == '/data/engage/process_e/'
	assert __standard.gDsEngProcessF == '/data/engage/process_f/'


def test_datetime():
	assert __standard.duration == 2
	assert __standard.end_date is None
	assert __standard.end_date_time is None
	assert __standard.end_time is None
	assert __standard.interval_hours == 1
	assert __standard.interval_minutes == '05'
	assert __standard.schedule_job_arr == ['CHAIN', 'day', '06', '05', 'CHANGE', 'friday', '06', '10']
	assert __standard.schedule_job_chain == ['CHAIN', 'day', '06', '05']
	assert __standard.schedule_job_change == ['CHANGE', 'friday', '06', '10']
	# assert __standard.sleep_seconds == 300
	assert __standard.sleep_seconds == 15
	assert __standard.start_date is None
	assert __standard.start_date_time is None
	assert __standard.start_time is None


def test_email():
	assert __standard.email_msg_status_from_arr == ['sas.ci360.automation.engine@gmail.com', 'None', 'None']
	assert __standard.email_msg_status_from == 'sas.ci360.automation.engine@gmail.com'
	assert __standard.email_msg_status_to_arr == ['nelson.mark.a@gmail.com', 'SAS360CHAINING@1fbusa.com', 'SAS360CHAINING@1fbusa.com']
	assert __standard.email_msg_status_to == 'nelson.mark.a@gmail.com'
	assert __standard.email_msg_support_from == 'sas.ci360.automation.engine@gmail.com'
	assert __standard.email_msg_support_to == 'nelson.mark.a@gmail.com'
	assert __standard.email_msg_support_cc == 'nelson.mark.a@gmail.com'
	assert __standard.email_server == 'smtp.gmail.com'
	assert __standard.email_server_login == 'sas.ci360.automation.engine@gmail.com'
	assert __standard.email_server_password == 'H*9p%4F#2bN'
	assert __standard.email_server_port == '465'


def test_files():
	assert __standard.export_file == 'SAS1FBCHAIN.CSV'
	assert __standard.export_change_file == 'SAS1FBCHANGE.CSV'


def test_flags():
	assert __standard.flag_append is True
	assert __standard.flag_clean_files is True
	assert __standard.flag_csv is True
	assert __standard.flag_csv_header is True
	assert __standard.flag_test_export is True
	assert __standard.flag_test_report is True


def test_identities():
	assert __standard.identity_bridge_table_id == '19ec53a0-8fdf-4ac1-9649-14168ef980a6'
	assert __standard.identity_value == 'None'
	assert __standard.secret_key_arr == ['ODcxODE0bGkzaTNoMzM3MjdtZzJpMWpoY2M5ZTloaDY4', 'MTkwNjEzMjNsN2w0a2FrbWVjZ2c2aGVrNzg4YWkzbTMxZzY=', 'MjAwMTIxMTJoNGMxMWs2OTUwbWw2bGpkNmFpbmNuMDI0NTY=']
	assert __standard.secret_key == 'ODcxODE0bGkzaTNoMzM3MjdtZzJpMWpoY2M5ZTloaDY4'
	assert __standard.tenant_id_arr == ['dd0c73c9fe00013c617772f8', '8aa616e33200010a560015fd', '0598684a0600010e2eb24714']
	assert __standard.tenant_id == 'dd0c73c9fe00013c617772f8'


def test_paths():
	assert __standard.analytic_services_controller_path == '/marketingData/analytic'
	assert __standard.analytic_transfer_controller_path == '/marketingData/analytic/transfers'
	assert __standard.bulk_load_external_events_path == '/marketingGateway/bulkEventsFileLocation'
	assert __standard.customer_jobs_path == '/marketingData/customerJobs'
	assert __standard.discover_service_path == '/marketingGateway/discoverService/dataDownload/eventData'
	assert __standard.event_jobs_path == '/marketingData/eventJobs'
	assert __standard.export_path == '/data/export/development/'
	assert __standard.export_post_path == 'D:/Clients/First_Financial/SAS360/CHAINING/DEVELOPMENT'
	assert __standard.export_request_jobs_path == '/marketingData/exportRequestJobs'
	assert __standard.export_tables_path == '/dbtReport,/detail/partitionedData,/detail/nonPartitionedData'
	assert __standard.external_gateway_path == 'extapigwservice-training.ci360.sas.com'
	assert __standard.file_transfer_location_path == '/marketingData/fileTransferLocation'
	assert __standard.identity_records_path == '/marketingData/identityRecords'
	assert __standard.import_path == '/marketingData/marketingData'
	assert __standard.import_request_jobs_path == '/marketingData/importRequestJobs'
	assert __standard.marketing_data_path == '/marketingData'
	assert __standard.marketing_gateway_path == '/marketingGateway'
	assert __standard.reports_path == '/reports/development/'
	assert __standard.tables_path == '/marketingData/tables'


def test_settings():
	assert __standard.agent_name_arr == ['DiscoverDownload', 'DiscoverConfirm', 'DiscoverConfirm']
	assert __standard.agent_name == 'DiscoverDownload'
	assert __standard.algorithm == 'HS256'
	assert __standard.dataset_name_arr == ['detail', 'identity', 'dbtReport']
	assert __standard.dataset_name == 'dbtReport'
	assert __standard.delimiter == '|'
	assert __standard.encoding == 'UTF-8'
	assert __standard.mode_name_arr == ['development']
	# assert __standard.mode_name_arr == ['development', 'test', 'production']
	assert __standard.mode_name == 'development'
	assert __standard.schema_version == '3'
	assert __standard.tenant_environment_arr == ['abcdefgh', 'ciffbust', 'ciffbkus']
	assert __standard.tenant_environment == 'abcdefgh'
	assert __standard.tenant_name_arr == ['GCIE PSD Regional US', '1st Financial Bank USA Production Tenant', '1st Financial Bank USA']
	assert __standard.tenant_name == 'GCIE PSD Regional US'
	assert __standard.tenant_number_arr == ['123456', '1906132', '2001211']
	assert __standard.tenant_number == '123456'
	assert __standard.tenant_product_arr == ['SAS Customer Intelligence 360', 'SAS Customer Intelligence 360', 'SAS Customer Intelligence 360']
	assert __standard.tenant_product == 'SAS Customer Intelligence 360'
	assert __standard.tenant_url_arr == ['https://platform-training.ci360.sas.com/SASCustomerIntelligenceHome/', 'https://platform-use.ci360.sas.com/SASCustomerIntelligenceHome/', 'https://platform-use.ci360.sas.com/SASCustomerIntelligenceHome/']
	assert __standard.tenant_url == 'https://platform-training.ci360.sas.com/SASCustomerIntelligenceHome/'
