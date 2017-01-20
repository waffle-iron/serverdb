import ipaddress, logging
from logging.handlers import RotatingFileHandler

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

def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=10000000,
                                  backupCount=2)
    logger.addHandler(handler)
