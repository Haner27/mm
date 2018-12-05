import os


class EnvConfig:
    """
    环境变量
    """
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    STATIC_DIR = os.path.join(ROOT_DIR, 'static')

    TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
    TEMPLATES_DOCS_DIR = os.path.join(TEMPLATES_DIR, 'docs')
    TEMPLATES_DOCS_API_DIR = os.path.join(TEMPLATES_DOCS_DIR, 'apis')

    TEMPLATES_REPORTS_DIR = os.path.join(TEMPLATES_DIR, 'reports')

    CONFIG_DIR = os.path.join(ROOT_DIR, 'configs')

    API_DIR = os.path.join(ROOT_DIR, 'apis')

    TEST_DIR = os.path.join(ROOT_DIR, 'test')
    TEST_CASES_DIR = os.path.join(TEST_DIR, 'cases')
    TEST_TEST_REPORT_DIR = os.path.join(TEST_DIR, 'reports')
