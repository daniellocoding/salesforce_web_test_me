import sys
from os.path import dirname, abspath

import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import auto_setup
from airtest.report.report import LogToHtml, simple_report


project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)


def run_pytest(file):

    if not cli_setup():
        auto_setup(__file__, logdir=f'{project_path}\\log')

    pytest.main(
        ["-sq", fr"{project_path}\\TestCase\\{file}.py", "--alluredir=.\\report", "--clean-alluredir"])

    html = LogToHtml(script_root=f'{project_path}\\TestCase\\{file}.py', script_name=f'{file}',
                     log_root=f'{project_path}\\log', export_dir=f'{project_path}\\AirtestReport',
                     logfile=f'{project_path}\\log\\log.txt', lang='zh', plugins=["airtest_selenium.report"])
    html.report()

if __name__ == '__main__':
    test_cases = [
        # 'test_ServiceConsole',

        # 'test_Login',
        # 'test_ClientToServer',        # Test Case 1
        # 'test_FreeTextMessaging',     # Test Case 2 + 5 (Template loading with changes to fields)
        # 'test_BulkMessaging',         # Test Case 3
        # 'test_BulkMessagesFromCsv',   # Test Case 4
        'test_WaitMessages',          # Test Case 7, 8, 9
        # 'test_ENameCard',             # Test Case 12

    ]
    for case in test_cases:
        run_pytest(case)
