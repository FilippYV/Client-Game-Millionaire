class MyException(Exception):
    pass


class FailedToConnect(MyException):
    pass


class FailedToGetUserId(MyException):
    pass