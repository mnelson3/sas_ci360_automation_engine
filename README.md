# SAS Customer Intelligence 360

## SAS CI360 Automation Engine

### Overview

The Automation Engine downloads Discover data from the SAS Customer Intelligence 360 (CI360) datahub, filters
it against a set of business rules, and writes the result to a comma-separated-value (.csv) file that is
uploaded back to the CI360 datahub as an Identity Bridge import. It runs as a long-lived background process
(a Linux systemd service, a Windows service, or a Docker container) that watches for new export files and
uploads/reports on a schedule.
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#configuration">Configuration</a>
 - <a href="#running-the-engine">Running the Engine</a>
 - <a href="#project-layout">Project Layout</a>
 - <a href="#testing">Testing</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.9
 * A SAS CI360 tenant with Discover and Identity Bridge configured
<br><br>

### Installation

 1. `git clone https://github.com/mnelson3/sas_ci360_automation_engine.git`
 1. `cd sas_ci360_automation_engine`
 1. `make venv` &mdash; creates a `venv/` virtual environment and installs `requirements.txt`
 1. On Windows only, also run `make win-venv` to install the `pywin32` dependencies needed by
    `src/SASCI360Service.py`
<br><br>

### Configuration

The engine reads its settings from `config/config.ini`, which is not committed to source control because it
holds per-tenant paths, credentials, and email addresses.

 1. `cp config/config.ini.example config/config.ini`
 1. Edit `config/config.ini` and fill in the `[EMAIL]`, `[IDENTITIES]`, `[PATHS]`, and `[SETTINGS]` values for
    your tenant and environment (`development`, `test`, `production`)

Each setting that varies by environment follows a `<name>_dev` / `<name>_test` / `<name>_prod` convention, with
an `<name>_arr` key listing all three and a plain `<name>` key resolving to whichever one the engine was
started with.
<br><br>

### Running the Engine

**As a Linux systemd service**
 1. Copy the project to `/opt/sas_ci360_automation_engine` (or update the paths in the `.service` file to
    match wherever you deploy it)
 1. `sudo cp sas_ci360_automation_engine.service /etc/systemd/system`
 1. `sudo systemctl daemon-reload`
 1. `sudo systemctl enable --now sas_ci360_automation_engine`
 1. `sudo systemctl status sas_ci360_automation_engine`

**As a Windows service**

`src/SASCI360Service.py` wraps the engine with `pywin32`'s `win32serviceutil`:
 1. `venv\Scripts\python.exe src\SASCI360Service.py install`
 1. `venv\Scripts\python.exe src\SASCI360Service.py start`

**With Docker**
 1. `docker compose up --build`

The `config/`, `data/`, and `logs/` directories are mounted into the container so the engine reads/writes the
same files it would on a bare-metal install.

**Directly, for local development**
 1. `make run`
<br><br>

### Project Layout

 - `src/main` - Process entry point; starts the chain/change schedulers and the file listener
 - `src/scheduler` - Runs the export/upload jobs on a recurring schedule
 - `src/listener` - Watches the export directory for new files and relays them
 - `src/custom` - The Identity Bridge upload, report, and status/support-messaging jobs that `listener` and
   `scheduler` invoke
 - `src/connection` - REST API client used to talk to CI360
 - `src/communication` - Sends status/support email notifications
 - `src/reporter` - Persists JSON responses to disk
 - `src/security` - Generates the JWTs used to authenticate CI360 API calls
 - `src/standard` - Loads `config/config.ini` and cleans/transforms exported data
 - `src/log` - Shared logging configuration
<br><br>

### Testing

 1. `make test-venv` &mdash; installs `requirements-test.txt` into `venv/`
 1. `cp config/config.ini.example config/config.ini` (if you haven't already)
 1. `make test`

Most of the tests under `tests/` are integration tests written against a live CI360 tenant's configuration
values (secret keys, tenant IDs, real email addresses); they will fail against the placeholder values in
`config.ini.example`. That's expected outside of a fully-configured tenant &mdash; CI runs the same suite so
regressions in code that doesn't depend on live credentials are still caught.
<br><br>

### Troubleshooting

For issues specific to a CI360 tenant's Discover or Identity Bridge configuration, consult your CI360
administrator. For issues with the engine itself, check `logs/` first &mdash; each module logs to its own
file there.
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit
contributions to this project.
<br><br>

### License

This project is licensed under the [Apache 2.0 License](LICENSE).
<br><br>

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
