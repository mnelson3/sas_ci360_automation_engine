#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from scheduler import Scheduler


def test_run_mode():
	mode = 'development'
	scheduler = Scheduler.Scheduler(mode=mode)
	scheduler.chain_run()
	scheduler.change_run()


def test_run():
	scheduler = Scheduler.Scheduler()
	scheduler.chain_run()
	scheduler.change_run()
