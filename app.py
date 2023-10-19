from CellSegmentation.logger import logging
from CellSegmentation.exception import AppException
import sys

logging.info("Welcome to custom log")

try:
    a=4/"6"
except Exception as e:
    raise AppException(e, sys)