# make venv, make unix-venv, make test-unix-venv, etc.

venv:
	virtualenv venv
	/venv/bin/python3 -m pip3 install -r ./requirements.txt

unix-venv: venv
	/venv/bin/python3 -m pip3 install -r ./requirements_unix.txt

test-unix-venv: venv
	/venv/bin/python3 -m pip3 install -r ./requirements_unix_test.txt

win-venv: venv
	/venv/bin/python3 -m pip3 install -r ./requirements_win.txt

test-win-venv: venv
	/venv/bin/python3 -m pip3 install -r ./requirements_win_test.txt
