from pydantic import BaseModel


class RequestModel(BaseModel):
    ip_address: str
    countries: list[str]


class ResponseModel(BaseModel):
    valid: bool
