# make venv, make win-venv, make test-venv, make test, make run

venv:
	python3 -m venv venv
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/python3 -m pip install -r requirements.txt

win-venv: venv
	venv/bin/python3 -m pip install -r requirements_win.txt

test-venv: venv
	venv/bin/python3 -m pip install -r requirements-test.txt

test: test-venv
	venv/bin/python3 -m pytest tests/

run: venv
	mkdir -p logs
	PYTHONPATH=src venv/bin/python3 -m main.Main
