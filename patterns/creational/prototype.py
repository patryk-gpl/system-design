""" Prototype design patterns examples """
from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods,


class Prototype:
    """A basic implementation of the Prototype design pattern"""

    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name):
        """Clone an object"""
        old_obj = self._objects.get(name)
        new_obj = old_obj.__class__()
        new_obj.__dict__.update(old_obj.__dict__)
        return new_obj


class Animal(ABC):
    """Animal base class"""

    @abstractmethod
    def speak(self):
        """Make a sound"""


class Dog(Animal):
    """A Dog class"""

    def speak(self):
        return "hau hau.."


class Cat(Animal):
    """A cat class"""

    def speak(self):
        return "meow meow.."
