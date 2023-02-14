""" Tests to check validity of Prototype design pattern """
import patterns.creational.prototype as pattern


class TestPrototypeClass:
    """Test Prototype design patterns various examples"""

    def test_clone_dog_instance(self):
        """Test whether Dog clone is identical"""
        p = pattern.Prototype()
        cat1 = pattern.Cat()
        p.register("cat", cat1)
        cat2 = p.clone("cat")
        cat2.speak()
        assert cat1.speak() == cat2.speak()
