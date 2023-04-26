from consts import ERROR_CODE, EXCEPTION_CODE


class ApiException(Exception):
    code = EXCEPTION_CODE
    msg = ERROR_CODE[EXCEPTION_CODE]
    debug_info = None

    def __init__(self, code=None, msg=None, debug_info=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if debug_info:
            self.debug_info = str(type(debug_info)) + ":" + str(debug_info)

    def to_result(self):
        if self.debug_info:

            return {'result_code': self.code, 'msg': self.msg, "debug_info": self.debug_info}
        else:
            return {'result_code': self.code, 'msg': self.msg}
