from fastapi import Request
from fastapi.security import HTTPBearer


# This is a stub that would be used in the future to add authorization to the endpoint
class Authorization(HTTPBearer):
    def __init__(self, perms: [str], auto_error: bool = True):
        self.needed_perms = perms
        super(Authorization, self).__init__(auto_error=auto_error)

    def __call__(self, request: Request):
        # this is where I would get the bearer token from the request and make sure the call was authorized
        pass
