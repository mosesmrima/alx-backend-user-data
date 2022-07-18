#!/usr/bin/env python3
""" this module contains functions to encryot and obfuscate data """
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    this function obfuscicates a log message
    """
    tmp = message
    for f in fields:
        tmp = re.sub(f +
                     "=.*?" + separator, f + "=" + redaction + separator, tmp)

    return tmp
