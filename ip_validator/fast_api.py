from logging import log, ERROR

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from .models import ResponseModel, RequestModel
from .service import ip_validator
from .service.authorizer_service import Authorization

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post('/validateip',
          status_code=200,
          dependencies=[Depends(Authorization(perms=[]))],
          response_model=ResponseModel)
async def validate_ip_address(request_body: RequestModel = None):
    if request_body is None:
        raise HTTPException(status_code=400, detail='Missing Request Body')

    try:
        ip_address = request_body.ip_address
        countries = request_body.countries

        is_valid = ip_validator.validate_ip_address(ip_address, countries)

        return ResponseModel(valid=is_valid)
    except Exception as e:
        log(ERROR, f'Exception determining if IP Address is valid. Exception: {str(e)}')
        raise HTTPException(status_code=500, detail='Exception determining if IP Address is valid.')
