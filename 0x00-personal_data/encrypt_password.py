#!/usr/bin/env python3
""" this module contains 2 functions """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash string   """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    compare hash and password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
