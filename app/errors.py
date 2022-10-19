class Errors(Exception):
    pass


class FailFileUsers(Errors):
    pass


class FailUserName(Errors):
    pass


class FailServerError(Errors):
    pass


class CommandNotFound(Errors):
    pass


class ErrorInput(Errors):
    pass
