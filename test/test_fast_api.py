import pytest
from fastapi import HTTPException

from ip_validator import fast_api as fa


@pytest.mark.asyncio
async def test_validate_ip_address_success():
    model = fa.RequestModel(
        ip_address='128.101.101.101',
        countries=['US', 'CA']
    )

    actual = await fa.validate_ip_address(model)

    assert type(actual) is fa.ResponseModel
    assert actual.valid is True


@pytest.mark.asyncio
async def test_validate_ip_address_no_body():
    with pytest.raises(HTTPException) as e:
        await fa.validate_ip_address()

    assert e.value.status_code == 400
    assert e.value.detail == 'Missing Request Body'


@pytest.mark.asyncio
async def test_validate_ip_address_exception(monkeypatch, caplog):
    model = fa.RequestModel(
        ip_address='128.101.101.101',
        countries=['US', 'CA']
    )

    def mock_validate_ip_address(*args, **kwargs):
        raise Exception('BOOM')

    monkeypatch.setattr(fa.ip_validator, 'validate_ip_address', mock_validate_ip_address)

    captured = caplog.records

    with pytest.raises(HTTPException) as e:
        await fa.validate_ip_address(model)

    assert e.value.status_code == 500
    assert e.value.detail == 'Exception determining if IP Address is valid.'
    assert 'Exception determining if IP Address is valid. Exception: BOOM' in str(captured)
