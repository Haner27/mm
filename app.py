from flask import Flask, url_for


def register_blueprints(app):
    from apis.user_api import user_app
    app.register_blueprint(user_app)


def validate_api_defined_field(app):
    for rule in app.url_map.iter_rules():
        view_func = app.view_functions.get(rule.endpoint)
        check_defined_field(rule.rule, view_func)


def check_defined_field(rule, view_func):
    if hasattr(view_func, 'api_doc_body_fields'):
        for api_doc_body_field in view_func.api_doc_body_fields or []:
            try:
                api_doc_body_field.validate()
            except Exception as e:
                raise Exception('[{0}][api_doc_body_field]{1}'.format(rule, e))

    if hasattr(view_func, 'api_doc_args_fields'):
        for api_doc_args_field in view_func.api_doc_args_fields or []:
            try:
                api_doc_args_field.validate()
            except Exception as e:
                raise Exception('[{0}][api_doc_args_field]{1}'.format(rule, e))


def app_check_api_field_func(app):
    for key in app.blueprints:
        if key not in app.before_first_request_funcs:
            app.before_request_funcs[key] = []


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    register_blueprints(app)

    # 检查api字段的定义
    validate_api_defined_field(app)

    # 统一给蓝图添加before_request_funcs
    app_check_api_field_func(app)
    return app
