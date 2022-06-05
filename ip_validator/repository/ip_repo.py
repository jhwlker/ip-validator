import geoip2.database
import os
from logging import log, ERROR


def get_ip_country(ip_address):
    try:
        with geoip2.database.Reader(os.path.join(os.path.dirname(__file__), 'db/GeoLite2-Country.mmdb')) as reader:
            response = reader.country(ip_address)
            return response.country.iso_code if response else ""
    except Exception as e:
        log(ERROR, f'Exception getting database. Exception: {str(e)}')
        return ""
