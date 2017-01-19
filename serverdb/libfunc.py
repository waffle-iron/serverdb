import ipaddress, logging


def ip_is_valid(host):
    """checks for a valid host ip"""
    try:
        logging.debug('checking if ip is valid...')
        ipv4address(str(host))
        valid = True
        logging.debug('Valid!')
        return valid
    except:
        valid = False
        logging.warning('Ip not valid!')
        return valid
