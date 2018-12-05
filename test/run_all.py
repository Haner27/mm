import os
from datetime import datetime

from HTMLReport import TestRunner
from unittest import TestSuite, TestLoader

from configs import EnvConfig

now = datetime.now()
test_case_dir = EnvConfig.TEST_CASES_DIR
report_file_name = 'unittest-{0}'.format(now.strftime('%Y%m%d%H%M%S'))
report_file_output = EnvConfig.TEST_TEST_REPORT_DIR

suite = TestSuite()  # 创建测试套件
loader = TestLoader()  # 创建测试用例加载器
suite.addTests(loader.discover(test_case_dir))  # 添加指定目录下的测试用例到测试套件中

runner = TestRunner(report_file_name=report_file_name,
                    output_path=report_file_output,
                    title='mm api服务',
                    description='项目整体进行单元测试',
                    thread_count=3,
                    sequential_execution=True
                    )
runner.run(suite)