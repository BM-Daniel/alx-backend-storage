#!/usr/bin/env python3

'''
0. Writing strings to Redis 
'''

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    '''Call history function'''
    key = method.__qualname__
    inputs = key + ':inputs'
    outputs = key + ':outputs'

    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    
    return wrapper

def count_calls(method: Callable) -> Callable:
    '''Count calls functtion'''
    key = method.__qualname__

    def wrapper(self, *args, **kwargs):
        '''Wrapper function'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

class Cache:
    '''Cache class'''
    def __init__(self):
        '''
        In the __init__ method, store an instance of the Redis client as a private
        variable named _redis (using redis.Redis()) and flush the instance
        using flushdb
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Create a store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid), store the
        input data in Redis using the random key and return the key.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''Get function'''
        data = self._redis.get(key)

        if fn:
            return fn(data)
        
        return data
    
    def get_str(self, key: str) -> str:
        '''Get function'''
        data = self._redis.get(key)

        try:
            data: int(value.decode('utf-8'))
        except Exception:
            data = 0

        return data
