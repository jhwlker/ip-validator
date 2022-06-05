from ip_validator.repository import ip_repo


def test_get_ip_country_success():
    actual = ip_repo.get_ip_country('128.101.101.101')
    assert actual == 'US'


def test_get_ip_country_except(caplog):
    captured = caplog.records

    actual = ip_repo.get_ip_country('totally bad')

    assert actual == ''
    assert 'Exception getting database. Exception: ' in str(captured)
