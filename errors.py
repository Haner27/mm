class ApiError(Exception):
    ERROR_API_BODY_PARAM_ERROR = 100
    ERROR_API_ARGS_PARAM_ERROR = 101
    ERROR_API_INTERNAL_ERROR = 200
    ERROR_API_FIELD_REQUIRED = 300
    ERROR_API_FIELD_TYPE_ERROR = 301
    ERROR_API_UNKNOWN = 999

    ERRORS = {
        ERROR_API_BODY_PARAM_ERROR: '接口body参数错误',
        ERROR_API_ARGS_PARAM_ERROR: '接口args参数错误',
        ERROR_API_INTERNAL_ERROR: '接口内部错误',
        ERROR_API_FIELD_REQUIRED: '字段必填',
        ERROR_API_FIELD_TYPE_ERROR: '字段类型错误',
        ERROR_API_UNKNOWN: '接口未知错误'
    }

    def __init__(self, msg, code=None, extras=None):
        """
        :param msg: 具体错误信息
        :param code: 错误码
        :param extras:
        """
        self.msg = msg
        if code not in self.ERRORS:
            code = self.ERROR_API_UNKNOWN

        self.code = code
        self.code_error = self.ERRORS.get(self.code)
        self.extras = extras
        error_msg = '[{0}][{1}]{2}'.format(self.code, self.code_error, self.msg)
        super(ApiError, self).__init__(error_msg)


class ApiBodyFieldError(ApiError):
    def __init__(self, msg):
        code = self.ERROR_API_BODY_PARAM_ERROR
        super(ApiBodyFieldError, self).__init__(msg, code)


class ApiArgsFieldError(ApiError):
    def __init__(self, msg):
        code = self.ERROR_API_ARGS_PARAM_ERROR
        super(ApiArgsFieldError, self).__init__(msg, code)


class ApiFieldRequiredError(ApiError):
    def __init__(self, msg):
        code = self.ERROR_API_FIELD_REQUIRED
        super(ApiFieldRequiredError, self).__init__(msg, code)


class ApiFieldTypeError(ApiError):
    def __init__(self, msg):
        code = self.ERROR_API_FIELD_TYPE_ERROR
        super(ApiFieldTypeError, self).__init__(msg, code)