from functools import wraps
from typing import List

from fastapi import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

from jwt_bearer import CognitoAuthenticator

auth = CognitoAuthenticator(
    pool_region="ap-south-1",
    pool_id='ap-south-1_oWdlm4cFH',
    client_id='4sqtfs7mqhjl6m1sfbqnjq6ea6',
)


def auth_required():
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request,*args, **kwargs):
            credentials = request.headers.get("Authorization", None) # Bearer token
            if credentials:
                try:
                    claims = auth.verify_token(credentials.split(' ')[1])
                    print(claims)
                except Exception as e:
                    print(e)
                    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
            else:
                raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

            return func(request,*args, **kwargs)

        return wrapper

    return decorator
