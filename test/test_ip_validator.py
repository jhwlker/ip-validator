from ip_validator.service import ip_validator as iv


def test_validate_ip_address_true(monkeypatch):
    countries = ['US', 'CA']

    def mock_get_ip_country(*args, **kwargs):
        return 'US'

    monkeypatch.setattr(iv.ip_repo, 'get_ip_country', mock_get_ip_country)

    actual = iv.validate_ip_address('128.101.101.101', countries)

    assert actual is True


def test_validate_ip_address_false(monkeypatch):
    countries = ['NZ', 'AU']

    def mock_get_ip_country(*args, **kwargs):
        return 'US'

    monkeypatch.setattr(iv.ip_repo, 'get_ip_country', mock_get_ip_country)

    actual = iv.validate_ip_address('128.101.101.101', countries)

    assert actual is False


def test_validate_ip_address_invalid(monkeypatch, caplog):
    countries = ['US', 'CA']

    captured = caplog.records

    actual = iv.validate_ip_address('timbuktu', countries)

    assert actual is False
    assert f'Invalid IP address submitted. IP Address = timbuktu. Exception: ' in str(captured)
