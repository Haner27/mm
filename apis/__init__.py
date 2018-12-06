from functools import wraps

from flask import jsonify, Blueprint, request

from errors import ApiBodyFieldError, ApiArgsFieldError, ApiFieldRequiredError, ApiFieldTypeError


def response(data):
    return jsonify(success=True, data=data)


def error(msg):
    return jsonify(success=False, error=msg)


class ApiFieldValidator:
    def __init__(self, field):
        self.field = field


class Required(ApiFieldValidator):
    def __call__(self, *args, **kwargs):
        if not self.field:
            raise ApiFieldRequiredError


class TypeCheck(ApiFieldValidator):
    def __call__(self, *args, **kwargs):
        example = self.field.example
        field_type = self.field.field_type
        if not isinstance(example, field_type):
            field_name = self.field.field_name
            msg = '字段{0}样例{1}不是{2}类型'.format(field_name, example, field_type)
            raise ApiFieldTypeError(msg)


class ApiField:
    def __init__(self, field_name, field_type, default, example, validators):
        self.field_name = field_name
        self.field_type = field_type
        self.default = default
        self.example = example
        self.validators = validators

    def validate(self):
        for validator in self.validators:
            validator(self)()


class ApiBodyField(ApiField):
    pass


class ApiArgsField(ApiField):
    pass


# api装饰器
class ApiDoc:
    API_DOC_DESCRIPTION = 'api_doc_description'
    API_DOC_BODY_FIELDS = 'api_doc_body_fields'
    API_DOC_ARGS_FIELDS = 'api_doc_args_fields'
    API_DOC_RETURN_OK = 'api_doc_return_ok'
    API_DOC_RETURN_ERROR = 'api_doc_return_error'

    @classmethod
    def add_description(cls, description):
        """
        添加API描述
        :param description: api描述
        :return:
        """
        def wrapper(func):
            setattr(func, cls.API_DOC_DESCRIPTION, description)

            @wraps(func)
            def decorate(*args, **kwargs):
                return func(*args, **kwargs)
            return decorate
        return wrapper

    @classmethod
    def add_body_field(cls, field_name, field_type=str, default=None, example='', validators=None):
        """
        添加body字段
        :param field_name: 字段名
        :param field_type: 字段类型
        :param default: 字段默认值
        :param example: 字段例子
        :param validators: 字段校验器列表,接受以字段为唯一参数的方法
        :return:
        """
        if not validators:
            validators = []

        def wrapper(func):
            if not hasattr(func, cls.API_DOC_BODY_FIELDS):
                setattr(func, cls.API_DOC_BODY_FIELDS, [])
            body_fields = getattr(func, cls.API_DOC_BODY_FIELDS)

            if field_name not in [f.field_name for f in body_fields]:
                if TypeCheck not in validators:
                    """参数检查默认加上"""
                    validators.append(TypeCheck)

                field = ApiBodyField(field_name=field_name,
                                     field_type=field_type,
                                     default=default,
                                     example=example,
                                     validators=validators)
                body_fields.append(field)
                setattr(func, cls.API_DOC_BODY_FIELDS, body_fields)

            @wraps(func)
            def decorate(*args, **kwargs):
                return func(*args, **kwargs)
            return decorate
        return wrapper

    @classmethod
    def add_args_field(cls, field_name, field_type=str, default=None, example='', validators=None):
        """
        添加args字段
        :param field_name: 字段名
        :param field_type: 字段类型
        :param default: 字段默认值
        :param example: 字段例子
        :param validators: 字段校验器列表,接受以字段为唯一参数的方法
        :return:
        """
        if not validators:
            validators = []

        def wrapper(func):
            if not hasattr(func, cls.API_DOC_ARGS_FIELDS):
                setattr(func, cls.API_DOC_ARGS_FIELDS, [])
            body_fields = getattr(func, cls.API_DOC_ARGS_FIELDS)

            if field_name not in [f.field_name for f in body_fields]:
                if TypeCheck not in validators:
                    """参数检查默认加上"""
                    validators.append(TypeCheck)

                field = ApiBodyField(field_name=field_name,
                                     field_type=field_type,
                                     default=default,
                                     example=example,
                                     validators=validators)
                body_fields.append(field)
                setattr(func, cls.API_DOC_ARGS_FIELDS, body_fields)

            @wraps(func)
            def decorate(*args, **kwargs):
                return func(*args, **kwargs)
            return decorate
        return wrapper

    @classmethod
    def add_return(cls):
        pass

