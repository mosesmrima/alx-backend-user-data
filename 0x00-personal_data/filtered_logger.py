#!/usr/bin/env python3
""" this module contains functions to encryot and obfuscate data """
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "password", "ssn", "phone")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    this function obfuscicates a log message
    """
    tmp = message
    for f in fields:
        tmp = re.sub(f + "=.*?" + separator,
                     f + "=" + redaction + separator, tmp)

    return tmp


def get_logger() -> logging.Logger:
    """Returns logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values in incoming log records"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR,
        )
