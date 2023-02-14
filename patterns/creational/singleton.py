""" Singleton design patterns examples """
# pylint: disable=missing-class-docstring, too-few-public-methods, broad-exception-raised

import functools
import threading
from functools import singledispatch


# Example 1
class Singleton:
    """A simple Singleton class"""

    _instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is None:
            Singleton._instance = self


# Example 2
class SingletonMeta(type):
    """A simple singleton class of a new type"""

    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class MySingletonMeta(metaclass=SingletonMeta):
    """A simple class that derives from SingletonMeta"""


# Example 3
class SingletonNew:
    """A simple singleton class to use __new__ method to construct a new instance"""

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Example 4
def singleton_decorator(cls):
    """A singleton method to be used as a decorator"""
    _instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton_decorator
class SingletonDecorated:
    """A simple class that is decorated with singleton method"""


# Example 5
@singledispatch
def singleton_dispatcher():
    """A singleton function decorated with singledispatch"""


@singleton_dispatcher.register(object)
class SingletonDispatcher:
    """A simple singleton dispatcher class"""

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Example 6
class SingletonThreadSafe:
    """A simple singleton thread safe class"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
