#!D:\Clients\First_Financial\SAS_CI360_Automation_Engine\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==2.5.2','console_scripts','py.test'
__requires__ = 'pytest==2.5.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytest==2.5.2', 'console_scripts', 'py.test')()
    )
