#!/usr/bin/env python3
"""" filtered logger """

from typing import List, Tuple
import re
import logging


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """ this function hide the data from the main """
    patern = "|".join(fields)
    return re.sub(f'({patern})=.*?{separator}', r'\g<1>' + "="
                  + redaction + separator, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    FIELDS: List[str]

    def __init__(self, fields: List[str]):
        """ The init method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """ The format method """
        return filter_datum(self.FIELDS, self.REDACTION,
                            super().format(record), self.SEPARATOR)
