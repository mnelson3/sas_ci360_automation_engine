#! /venv/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from unittest.mock import patch

from main import Main

# start() spawns a real multiprocessing.Process per mode for each of the
# scheduler chain, scheduler change, and listener loops - each of which
# runs while True: ... forever by design, for the live service. Calling
# start() unmocked leaves those child processes running after the test
# returns; pytest-timeout only bounds the test function itself, so the
# job never exits once the process tree includes an orphaned infinite
# loop. Mock Process so start() is exercised without ever spawning one.


@patch("main.Main.Process")
def test_run(mock_process):
	Main.start()

	assert mock_process.called
	for call in mock_process.call_args_list:
		assert call.kwargs["target"] in (
			Main.run_scheduler_chain,
			Main.run_scheduler_change,
			Main.run_listener,
		)
	mock_process.return_value.start.assert_called()
