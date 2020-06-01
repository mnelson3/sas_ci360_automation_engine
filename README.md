The SAS Customer Intelligence 360 (CI360) Automation Engine is designed to download Discover data from the CI360 datahub which
is hosted in the cloud. This data is then processed for records where that meet a predefined set of business rules. A new
comma-separated-value (.csv) data-file is created and uploaded back to the CI360 datahub.

The Automation Engine was developed in Python version 3.7 as a Unix service.

The directory structure is:
SAS_CI360_Automation_Engine/config          Contains the single configuration file
SAS_CI360_Automation_Engine/data_store      Contains the sub-directories where the data is processed
SAS_CI360_Automation_Engine/logs            Contains the error logs for the program
SAS_CI360_Automation_Engine/src             Contains the Python source files developed for the program
SAS_CI360_Automation_Engine/venv            Contains the Python virtual environment - python executable and required libraries

Setup and run Unix service
 - I assume you will need run everything as 'sudo'
 - Update the PATH(s) in the /SAS_CI360_Automation_Engine/src/sas_ci360_automation_engine.service to appropriate folder(s)
sudo cp -r /opt/SAS_CI360_Automation_Engine/src/sas_ci360_automation_engine.service /etc/systemd/system
sudo systemctl daemon-reload                                    Reloads the Unix daemon
sudo systemctl enable sas_ci360_automation_engine.service       Enables the service, sets the symlinks
sudo systemctl disable sas_ci360_automation_engine.service      Disables the service, destroys the symlinks
sudo systemctl start sas_ci360_automation_engine.service        Starts the service
sudo systemctl status sas_ci360_automation_engine.service       Status of the service
sudo systemctl stop sas_ci360_automation_engine.service         Stops the service
=======
# SAS_CI360_Automation_Engine

