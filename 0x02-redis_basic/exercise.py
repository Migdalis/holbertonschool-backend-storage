#!/usr/bin/env python3
""" Module to manage Redis client"""
from uuid import uuid4
import redis
from typing import Any


class Cache(object):
    """docstring for Cache."""

    def __init__(self):
        """ Create a new redis instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
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
        self._redis.bgsave()
        return key
