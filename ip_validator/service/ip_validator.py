import ipaddress

from ip_validator.repository import ip_repo
from logging import log, ERROR


def validate_ip_address(ip_address, countries):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError as e:
        log(ERROR, f'Invalid IP address submitted. IP Address = {ip_address}. Exception: {str(e)}')
        return False

    country = ip_repo.get_ip_country(ip_address)

    return country in countries
