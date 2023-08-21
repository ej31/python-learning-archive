import logging

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("An exception occurred")
