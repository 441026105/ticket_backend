USER_ROLE = {
    "ADMIN": 0,
    "USER": 1
}
ERROR_CODE = {
    10000: "请求失败",
    10101: "{}账号不存在",
    10102: "{}账号密码输入错误，{}次后将会锁定账号{}分钟",
    10103: "{}账号已被锁定{}分钟",
    10104: "{} not found",
    10105: "请求超时，请重新登录",
    10106: "没有权限",
    10201: "{} required",
    10202: "access_token not found",
    10203: "{} not in choices",
    10204: "method not allowed",
    10401: "类型错误",

}

EXCEPTION_CODE = 10000
SUCCESS_CODE = 2000
JWT_KEY = '0x5f3759df'
JWT_TOKEN_LIFE = 24
JWT_REFRESH_TOKEN_LIFE = 48
LOGIN_ERROR_LOCKED_TIME = 60  # minutes
LOGIN_ERROR_LIMITED_TIMES = 10  # minutes
