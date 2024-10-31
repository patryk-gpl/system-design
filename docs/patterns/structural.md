- [Structural Design Patterns](#structural-design-patterns)
  - [Adapter](#adapter)
    - [Description](#description)
    - [When to Use](#when-to-use)
    - [Key Components](#key-components)
    - [Python Example](#python-example)
    - [Advantages and Drawbacks](#advantages-and-drawbacks)
  - [Bridge](#bridge)
    - [Description](#description-1)
    - [When to Use](#when-to-use-1)
    - [Key Components](#key-components-1)
    - [Python Example](#python-example-1)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-1)
  - [Composite](#composite)
    - [Description](#description-2)
    - [When to Use](#when-to-use-2)
    - [Key Components](#key-components-2)
    - [Python Example](#python-example-2)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-2)
  - [Decorator](#decorator)
    - [Description](#description-3)
    - [When to Use](#when-to-use-3)
    - [Key Components](#key-components-3)
    - [Python Example](#python-example-3)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-3)
  - [Facade](#facade)
    - [Description](#description-4)
    - [When to Use](#when-to-use-4)
    - [Key Components](#key-components-4)
    - [Python Example](#python-example-4)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-4)
  - [Flyweight](#flyweight)
    - [Description](#description-5)
    - [When to Use](#when-to-use-5)
    - [Key Components](#key-components-5)
    - [Python Example](#python-example-5)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-5)
  - [Proxy](#proxy)
    - [Description](#description-6)
    - [When to Use](#when-to-use-6)
    - [Key Components](#key-components-6)
    - [Python Example](#python-example-6)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-6)

# Structural Design Patterns

Structural design patterns are concerned with how classes and objects are composed to form larger structures. These patterns focus on simplifying the structure by identifying relationships between entities.

## Adapter

### Description
The Adapter pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces.

### When to Use
- When you want to use an existing class, but its interface doesn't match the one you need.
- When you want to create a reusable class that cooperates with unrelated or unforeseen classes.

### Key Components
- Target: Defines the domain-specific interface that Client uses.
- Adapter: Adapts the interface Adaptee to the Target interface.
- Adaptee: Defines an existing interface that needs adapting.
- Client: Collaborates with objects conforming to the Target interface.

### Python Example

```python
class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

class Socket(EuropeanSocketInterface):
    def voltage(self): return 230
    def live(self): return 1
    def neutral(self): return -1
    def earth(self): return 0

class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

class Adapter(USASocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self): return 110
    def live(self): return self.socket.live()
    def neutral(self): return self.socket.neutral()

# Usage
socket = Socket()
adapter = Adapter(socket)
print(f"Voltage from adapter: {adapter.voltage()}")
print(f"Live from adapter: {adapter.live()}")
print(f"Neutral from adapter: {adapter.neutral()}")
```

### Advantages and Drawbacks
Advantages:
- Allows incompatible classes to work together.
- Improves reusability of existing code.

Drawbacks:
- Can add complexity to the code.
- Sometimes many adaptations are required along an adapter chain to reach the type you want.

## Bridge

### Description
The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.

### When to Use
- When you want to avoid a permanent binding between an abstraction and its implementation.
- When both the abstractions and their implementations should be extensible by subclassing.

### Key Components
- Abstraction: Defines the abstraction's interface and maintains a reference to an object of type Implementor.
- RefinedAbstraction: Extends the interface defined by Abstraction.
- Implementor: Defines the interface for implementation classes.
- ConcreteImplementor: Implements the Implementor interface.

### Python Example

```python
from abc import ABC, abstractmethod

# Implementor
class DrawAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

# Concrete Implementors
class RedCircle(DrawAPI):
    def draw_circle(self, x, y, radius):
        return f"Drawing Red Circle at ({x}, {y}) with radius {radius}"

class BlueCircle(DrawAPI):
    def draw_circle(self, x, y, radius):
        return f"Drawing Blue Circle at ({x}, {y}) with radius {radius}"

# Abstraction
class Shape(ABC):
    def __init__(self, draw_api):
        self.draw_api = draw_api

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, draw_api):
        super().__init__(draw_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        return self.draw_api.draw_circle(self.x, self.y, self.radius)

# Usage
red_circle = Circle(100, 100, 10, RedCircle())
blue_circle = Circle(200, 200, 20, BlueCircle())

print(red_circle.draw())
print(blue_circle.draw())
```

### Advantages and Drawbacks
Advantages:
- Decouples interface from implementation.
- Improves extensibility and flexibility.

Drawbacks:
- Increases complexity.
- Can be overkill for simple scenarios.

## Composite

### Description
The Composite pattern composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

### When to Use
- When you want to represent part-whole hierarchies of objects.
- When you want clients to be able to ignore the difference between compositions of objects and individual objects.

### Key Components
- Component: Declares the interface for objects in the composition and implements default behavior.
- Leaf: Represents leaf objects in the composition. A leaf has no children.
- Composite: Defines behavior for components having children and stores child components.

### Python Example

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [f"Composite {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return '\n'.join(results)

# Usage
leaf1 = Leaf("1")
leaf2 = Leaf("2")
leaf3 = Leaf("3")

composite1 = Composite("C1")
composite1.add(leaf1)
composite1.add(leaf2)

composite2 = Composite("C2")
composite2.add(leaf3)
composite2.add(composite1)

print(composite2.operation())
```

### Advantages and Drawbacks
Advantages:
- Defines class hierarchies consisting of primitive and complex objects.
- Makes it easier to add new kinds of components.

Drawbacks:
- Can make the design overly general.

## Decorator

### Description
The Decorator pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

### When to Use
- When you want to add responsibilities to individual objects dynamically and transparently, without affecting other objects.
- When extension by subclassing is impractical or impossible.

### Key Components
- Component: Defines the interface for objects that can have responsibilities added to them dynamically.
- ConcreteComponent: Defines an object to which additional responsibilities can be attached.
- Decorator: Maintains a reference to a Component object and defines an interface that conforms to Component's interface.
- ConcreteDecorator: Adds responsibilities to the component.

### Python Example

```python
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 1.0

    def description(self):
        return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return f"{self._coffee.description()}, milk"

class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2

    def description(self):
        return f"{self._coffee.description()}, sugar"

# Usage
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost()}")

coffee_with_milk = Milk(coffee)
print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = Sugar(Milk(coffee))
print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")
```

### Advantages and Drawbacks
Advantages:
- More flexible than static inheritance.
- Avoids feature-laden classes high up in the hierarchy.

Drawbacks:
- Can result in many small objects in the design, which can be hard to debug.

## Facade

### Description
The Facade pattern provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

### When to Use
- When you want to provide a simple interface to a complex subsystem.
- When there are many dependencies between clients and the implementation classes of an abstraction.

### Key Components
- Facade: Provides a unified interface to a set of interfaces in a subsystem.
- Subsystem classes: Implement subsystem functionality and handle work assigned by the Facade object.

### Python Example

```python
class CPU:
    def freeze(self):
        return "Freezing processor"

    def jump(self, position):
        return f"Jumping to {position}"

    def execute(self):
        return "Executing"

class Memory:
    def load(self, position, data):
        return f"Loading data '{data}' to {position}"

class HardDrive:
    def read(self, lba, size):
        return f"Reading data from sector {lba} with size {size}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        results = [
            self.cpu.freeze(),
            self.memory.load("0x00", self.hard_drive.read("100", "1024")),
            self.cpu.jump("0x00"),
            self.cpu.execute()
        ]
        return "\n".join(results)

# Usage
computer = ComputerFacade()
print(computer.start())
```

### Advantages and Drawbacks
Advantages:
- Simplifies the interface to a complex subsystem.
- Decouples the subsystem from clients and other subsystems.

Drawbacks:
- Can become a "god object" coupled to all classes of an app.

## Flyweight

### Description
The Flyweight pattern uses sharing to support large numbers of fine-grained objects efficiently.

### When to Use
- When an application uses a large number of objects.
- When storage costs are high because of the sheer quantity of objects.
- When most object state can be made extrinsic.

### Key Components
- Flyweight: Declares an interface through which flyweights can receive and act on extrinsic state.
- ConcreteFlyweight: Implements the Flyweight interface and stores intrinsic state.
- FlyweightFactory: Creates and manages flyweight objects.

### Python Example

```python
import random

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        return f"Drawing {self.name} tree with {self.color} color and {self.texture} texture at ({x}, {y})"

class TreeFactory:
    tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = f"{name}-{color}-{texture}"
        if key not in cls.tree_types:
            cls.tree_types[key] = TreeType(name, color, texture)
        return cls.tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        return self.tree_type.draw(canvas, self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        return "\n".join([tree.draw(canvas) for tree in self.trees])

# Usage
forest = Forest()
for _ in range(10):
    forest.plant_tree(
        random.randint(0, 100),
        random.randint(0, 100),
        random.choice(["Oak", "Maple", "Pine"]),
        random.choice(["Green", "Dark Green", "Light Green"]),
        random.choice(["Smooth", "Rough", "Bark"])
    )

print(forest.draw("canvas"))
print(f"Tree types created: {len(TreeFactory.tree_types)}")
```

### Advantages and Drawbacks
Advantages:
- Reduces memory usage when many similar objects are used.
- Can greatly reduce the cost of complex object models.

Drawbacks:
- May introduce complexity in code.
- Can impact CPU performance in exchange for saving RAM.

## Proxy

### Description
The Proxy pattern provides a surrogate or placeholder for another object to control access to it.

### When to Use
- When you need a more versatile or sophisticated reference to an object than a simple pointer.
- For lazy initialization (virtual proxy).
- For access control (protection proxy).
- For local execution of a remote service (remote proxy).
- For logging requests (logging proxy).
- For caching request results (caching proxy).

### Key Components
- Subject: Defines the common interface for RealSubject and Proxy.
- RealSubject: Defines the real object that the proxy represents.
- Proxy: Maintains a reference that lets the proxy access the real subject.

### Python Example

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request."

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        return "Proxy: Access denied."

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)

print(proxy.request())
```

### Advantages and Drawbacks
Advantages:
- Controls access to the original object.
- Can perform optimizations like caching.
- Works even if the real subject is not ready or available.

Drawbacks:
- May add a level of indirection, potentially impacting performance.
- Code can become more complicated.

---

[Home](readme.md) | [Top](#structural-design-patterns)
