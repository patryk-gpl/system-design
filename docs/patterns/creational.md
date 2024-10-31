- [Creational Design Patterns](#creational-design-patterns)
  - [Singleton](#singleton)
    - [Description](#description)
    - [When to Use](#when-to-use)
    - [Key Components](#key-components)
    - [Python Example](#python-example)
    - [Advantages and Drawbacks](#advantages-and-drawbacks)
  - [Factory Method](#factory-method)
    - [Description](#description-1)
    - [When to Use](#when-to-use-1)
    - [Key Components](#key-components-1)
    - [Python Example](#python-example-1)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-1)
  - [Abstract Factory](#abstract-factory)
    - [Description](#description-2)
    - [When to Use](#when-to-use-2)
    - [Key Components](#key-components-2)
    - [Python Example](#python-example-2)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-2)
  - [Builder](#builder)
    - [Description](#description-3)
    - [When to Use](#when-to-use-3)
    - [Key Components](#key-components-3)
    - [Python Example](#python-example-3)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-3)
  - [Prototype](#prototype)
    - [Description](#description-4)
    - [When to Use](#when-to-use-4)
    - [Key Components](#key-components-4)
    - [Python Example](#python-example-4)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-4)

# Creational Design Patterns

Creational design patterns are concerned with the way objects are created, providing solutions to instantiate objects in the most suitable manner for specific situations. These patterns aim to increase flexibility and reusability of code.

## Singleton

### Description
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

### When to Use
- When exactly one instance of a class is needed to coordinate actions across the system.
- When you want to restrict object creation for certain classes to only one instance.

### Key Components
- Singleton class: The class that implements the singleton pattern.
- Private constructor: To prevent direct construction calls with the `new` operator.
- Static method: That returns the unique instance.

### Python Example

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def some_business_logic(self):
        pass

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

### Advantages and Drawbacks
Advantages:
- Ensures a class has only one instance.
- Provides a global access point to that instance.

Drawbacks:
- Can make unit testing difficult.
- Violates the Single Responsibility Principle.

## Factory Method

### Description
The Factory Method pattern defines an interface for creating an object but lets subclasses decide which class to instantiate.

### When to Use
- When a class can't anticipate the type of objects it needs to create.
- When a class wants its subclasses to specify the objects it creates.

### Key Components
- Creator: Declares the factory method.
- Concrete Creator: Overrides the factory method to return an instance of a Concrete Product.
- Product: Defines the interface of objects the factory method creates.
- Concrete Product: Implements the Product interface.

### Python Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Usage
dog_factory = DogFactory()
cat_factory = CatFactory()

dog = dog_factory.create_animal()
cat = cat_factory.create_animal()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

### Advantages and Drawbacks
Advantages:
- Provides flexibility in creating objects.
- Promotes loose coupling.

Drawbacks:
- Can lead to many small, similar classes.
- May complicate the code structure.

## Abstract Factory

### Description
The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

### When to Use
- When a system should be independent of how its products are created, composed, and represented.
- When you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.

### Key Components
- Abstract Factory: Declares an interface for operations that create abstract product objects.
- Concrete Factory: Implements the operations to create concrete product objects.
- Abstract Product: Declares an interface for a type of product object.
- Concrete Product: Defines a product object to be created by the corresponding concrete factory.
- Client: Uses only interfaces declared by Abstract Factory and Abstract Product classes.

### Python Example

```python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Products
class MacButton(Button):
    def paint(self):
        return "Rendered a MacOS button"

class MacCheckbox(Checkbox):
    def paint(self):
        return "Rendered a MacOS checkbox"

class WindowsButton(Button):
    def paint(self):
        return "Rendered a Windows button"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Rendered a Windows checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factories
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Client
def create_gui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button.paint(), checkbox.paint()

# Usage
mac_factory = MacFactory()
windows_factory = WindowsFactory()

print(create_gui(mac_factory))
print(create_gui(windows_factory))
```

### Advantages and Drawbacks
Advantages:
- Ensures compatibility between products.
- Isolates concrete classes.

Drawbacks:
- Difficult to add new kinds of products.
- Complexity increases with each new type of product.

## Builder

### Description
The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

### When to Use
- When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
- When the construction process must allow different representations for the object that's constructed.

### Key Components
- Builder: Specifies an abstract interface for creating parts of a Product object.
- Concrete Builder: Constructs and assembles parts of the product by implementing the Builder interface.
- Director: Constructs an object using the Builder interface.
- Product: Represents the complex object under construction.

### Python Example

```python
class Computer:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Computer parts: {', '.join(self.parts)}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.add("CPU")
        return self

    def add_memory(self):
        self.computer.add("Memory")
        return self

    def add_storage(self):
        self.computer.add("Storage")
        return self

    def build(self):
        return self.computer

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_minimal_computer(self):
        return self.builder.add_cpu().add_memory().build()

    def build_full_computer(self):
        return self.builder.add_cpu().add_memory().add_storage().build()

# Usage
director = Director()
builder = ComputerBuilder()
director.set_builder(builder)

minimal_computer = director.build_minimal_computer()
print(minimal_computer.list_parts())

full_computer = director.build_full_computer()
print(full_computer.list_parts())
```

### Advantages and Drawbacks
Advantages:
- Allows you to vary a product's internal representation.
- Isolates code for construction and representation.

Drawbacks:
- Requires creating a separate ConcreteBuilder for each different type of product.
- Requires the builder classes to be mutable.

## Prototype

### Description
The Prototype pattern specifies the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

### When to Use
- When a system should be independent of how its products are created, composed, and represented.
- When classes to instantiate are specified at run-time.
- To avoid building a class hierarchy of factories that parallels the class hierarchy of products.

### Key Components
- Prototype: Declares an interface for cloning itself.
- Concrete Prototype: Implements an operation for cloning itself.
- Client: Creates a new object by asking a prototype to clone itself.

### Python Example

```python
import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.make = "Ford"
        self.model = "Mustang"
        self.color = "Red"

    def __str__(self):
        return f"{self.make} {self.model} in {self.color}"

# Usage
car = Car()
prototype = Prototype()
prototype.register_object('car', car)

car1 = prototype.clone('car')
print(car1)  # Output: Ford Mustang in Red

car2 = prototype.clone('car', color="Blue", model="Explorer")
print(car2)  # Output: Ford Explorer in Blue
```

### Advantages and Drawbacks
Advantages:
- Reduces the need for subclassing.
- Hides complexities of creating new instances.
- Lets you add or remove objects at runtime.

Drawbacks:
- Overkill for a project that uses very few objects and/or does not have an underlying emphasis on the extension of prototype chains.
- Cloning complex objects that have circular references might be very tricky.

---

[Home](readme.md) | [Top](#creational-design-patterns)
