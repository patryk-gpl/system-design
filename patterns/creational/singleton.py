""" Singleton design patterns examples """
# pylint: disable=missing-class-docstring, too-few-public-methods, broad-exception-raised

import functools
import threading
from functools import singledispatch


# Example 1
class Singleton:
    """A simple Singleton class"""

    instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        return Singleton.instance

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = self


# Example 2
class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class MySingletonMeta(metaclass=SingletonMeta):
    pass


# Example 3
class SingletonNew:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


# Example 4
def singleton_decorator(cls):
    """A singleton method to be used as a decorator"""
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton_decorator
class SingletonDecorated:
    pass


# Example 5
@singledispatch
def singleton_dispatcher():
    """A singleton function"""


@singleton_dispatcher.register(object)
class SingletonDispatcher:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


# Example 6
class SingletonThreadSafe:
    instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls.instance:
            with cls._lock:
                if not cls.instance:
                    cls.instance = super().__new__(cls)
        return cls.instance
