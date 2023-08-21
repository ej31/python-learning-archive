import logging

logging.basicConfig(filename='example.log', level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Attempted to divide by zero")




