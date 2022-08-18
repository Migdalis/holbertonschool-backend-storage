#!/usr/bin/env python3
""" Module to manage Redis client"""
from functools import wraps
from uuid import uuid4
import redis
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """
        Method that count how many times methods of
        the Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function for decorator """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache(object):
    """ Redis class manage"""

    def __init__(self):
        """ Create a new redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Method that generate a random key,
            store the input data in Redis using the random key
            and return the key

            Args:
                data (Any): data to be storage

            Returns:
                The key generate
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
            Method that take a key string argument and an optional
            Callable argument named fn.
            This callable will be used to convert the data back to
            the desired format
        """
        rspns = self._redis.get(key)
        if fn:
            return fn(rspns)
        return rspns

    def get_str(self, key) -> str:
        """ Convert a key value to string """
        return self._redis.get(key, str)

    def get_int(self, key) -> int:
        """ Convert a key value to string """
        return self._redis.get(key, int)
