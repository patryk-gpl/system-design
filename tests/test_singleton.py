""" Tests to check validity of Singleton design pattern with various implementations """
from patterns.creational.singleton import (
    MySingletonMeta,
    Singleton,
    SingletonDecorated,
    SingletonDispatcher,
    SingletonNew,
    SingletonThreadSafe,
)


class TestSingletonClass:
    """Test Singleton design patterns various examples"""

    def test_instance_simple_class(self):
        """Test a simple class implementation"""
        singleton_1 = Singleton()
        singleton_2 = Singleton.get_instance()
        singleton_3 = Singleton.get_instance()

        assert singleton_1 == singleton_2
        assert singleton_2 == singleton_3

    def test_singleton_meta(self):
        """Test a Singleton object derived from metaclass"""
        singleton_1 = MySingletonMeta()
        singleton_2 = MySingletonMeta()
        assert singleton_1 is singleton_2

    def test_singleton_new(self):
        """Test a Singleton object derived from metaclass"""
        singleton_1 = SingletonNew()
        singleton_2 = SingletonNew()
        assert singleton_1 is singleton_2

    def test_singleton_decorated(self):
        """Test a singleton object decorated by a singleton function"""
        singleton_1 = SingletonDecorated()
        singleton_2 = SingletonDecorated()
        assert singleton_1 is singleton_2

    def test_singleton_dispatcher(self):
        """Test a singleton dispatcher method"""
        instance1 = SingletonDispatcher()
        instance2 = SingletonDispatcher()
        assert instance1 is instance2

    def test_singleton_thread_safe(self):
        """Test a singleton with thread-safe implementation"""
        instance1 = SingletonThreadSafe()
        instance2 = SingletonThreadSafe()
        assert instance1 is instance2
