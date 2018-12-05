from flask import Flask


def register_blueprints(app):
    pass


def create_app():
    app = Flask(__name__)

    #

    # 注册蓝图
    register_blueprints(app)
    return app