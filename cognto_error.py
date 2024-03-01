class CognitoError(Exception):
    pass

class InvalidJWTError(CognitoError):
    pass

class InvalidKidError(CognitoError):
    pass

class SignatureError(CognitoError):
    pass

class TokenExpiredError(CognitoError):
    pass


class InvalidIssuerError(CognitoError):
    pass


class InvalidAudienceError(CognitoError):
    pass


class InvalidTokenUseError(CognitoError):
    pass

class CognitoError(Exception):
    pass


