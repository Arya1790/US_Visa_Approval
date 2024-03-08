'''Exception'''
from us_visa.exception import USvisaException
from us_visa.logger import logging
import sys

try:
    x = 1/'a'
except Exception as e:
    logging.info(USvisaException(e, sys))
    raise USvisaException(e, sys) from e

''' logger test'''
"""
from us_visa.logger import logging

logging.info("test")"""