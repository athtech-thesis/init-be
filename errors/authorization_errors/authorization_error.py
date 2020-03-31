class UserNotFound(BaseException):
    def __init__(self, field, value):
        super(UserNotFound, self).__init__()
        self.message = "Couldn't found a user with {field}: {value}.".format(field=field, value=value)
        self.status = 404


class UserAlreadyExists(BaseException):
    def __init__(self, email):
        super(UserAlreadyExists, self).__init__()
        self.message = "User with email: {email} already exists.".format(email=email)
        self.status = 400


class WrongCredentials(BaseException):
    def __init__(self):
        super(WrongCredentials, self).__init__()
        self.message = "Wrong Username or Password"
        self.status = 400


class MissingData(BaseException):
    def __init__(self):
        super(MissingData, self).__init__()
        self.message = "Required data is missing"
        self.status = 400


class FormattingError(BaseException):
    def __init__(self):
        super(FormattingError, self).__init__()
        self.message = "Request has wrong format. All requests should be in JSON format"
        self.status = 406


class InitValidationError(BaseException):
    def __init__(self, message):
        super(InitValidationError, self).__init__()
        self.message = message
        self.status = 400


class TokenHasExpired(BaseException):
    def __init__(self):
        super(TokenHasExpired, self).__init__()
        self.message = "Token has expired"
        self.status = 400


class TokenNotFound(BaseException):
    def __init__(self):
        super(TokenNotFound, self).__init__()
        self.message = "Token not found"
        self.status = 400


class MoreThanOneTokensFound(BaseException):
    def __init__(self):
        super(MoreThanOneTokensFound, self).__init__()
        self.message = "More than one tokens found. Please contact support."
        self.status = 500
