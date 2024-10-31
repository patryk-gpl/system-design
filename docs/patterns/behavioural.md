- [Behavioral Design Patterns](#behavioral-design-patterns)
  - [Chain of Responsibility](#chain-of-responsibility)
    - [Description](#description)
    - [When to Use](#when-to-use)
    - [Key Components](#key-components)
    - [Python Example](#python-example)
    - [Advantages and Drawbacks](#advantages-and-drawbacks)
  - [Command](#command)
    - [Description](#description-1)
    - [When to Use](#when-to-use-1)
    - [Key Components](#key-components-1)
    - [Python Example](#python-example-1)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-1)
  - [Interpreter](#interpreter)
    - [Description](#description-2)
    - [When to Use](#when-to-use-2)
    - [Key Components](#key-components-2)
    - [Python Example](#python-example-2)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-2)
  - [Iterator](#iterator)
    - [Description](#description-3)
    - [When to Use](#when-to-use-3)
    - [Key Components](#key-components-3)
    - [Python Example](#python-example-3)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-3)
  - [Mediator](#mediator)
    - [Description](#description-4)
    - [When to Use](#when-to-use-4)
    - [Key Components](#key-components-4)
    - [Python Example](#python-example-4)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-4)
  - [Memento](#memento)
    - [Description](#description-5)
    - [When to Use](#when-to-use-5)
    - [Key Components](#key-components-5)
    - [Python Example](#python-example-5)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-5)
  - [Observer](#observer)
    - [Description](#description-6)
    - [When to Use](#when-to-use-6)
    - [Key Components](#key-components-6)
    - [Python Example](#python-example-6)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-6)
  - [State](#state)
    - [Description](#description-7)
    - [When to Use](#when-to-use-7)
    - [Key Components](#key-components-7)
    - [Python Example](#python-example-7)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-7)
  - [Strategy](#strategy)
    - [Description](#description-8)
    - [When to Use](#when-to-use-8)
    - [Key Components](#key-components-8)
    - [Python Example](#python-example-8)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-8)
  - [Template Method](#template-method)
    - [Description](#description-9)
    - [When to Use](#when-to-use-9)
    - [Key Components](#key-components-9)
    - [Python Example](#python-example-9)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-9)
  - [Visitor](#visitor)
    - [Description](#description-10)
    - [When to Use](#when-to-use-10)
    - [Key Components](#key-components-10)
    - [Python Example](#python-example-10)
    - [Advantages and Drawbacks](#advantages-and-drawbacks-10)

# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects. They describe not just patterns of objects or classes but also the patterns of communication between them.

## Chain of Responsibility

### Description
The Chain of Responsibility pattern passes requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

### When to Use
- When more than one object may handle a request, and the handler isn't known a priori.
- When you want to issue a request to one of several objects without specifying the receiver explicitly.

### Key Components
- Handler: Defines an interface for handling requests.
- ConcreteHandler: Handles requests it is responsible for and can access its successor.
- Client: Initiates the request to a ConcreteHandler object on the chain.

### Python Example

```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if 0 < request <= 10:
            print(f"ConcreteHandler1 handled request {request}")
        elif self._successor:
            self._successor.handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if 10 < request <= 20:
            print(f"ConcreteHandler2 handled request {request}")
        elif self._successor:
            self._successor.handle_request(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if 20 < request <= 30:
            print(f"ConcreteHandler3 handled request {request}")
        elif self._successor:
            self._successor.handle_request(request)

# Usage
handler3 = ConcreteHandler3()
handler2 = ConcreteHandler2(handler3)
handler1 = ConcreteHandler1(handler2)

requests = [2, 14, 22, 18, 3, 27]
for request in requests:
    handler1.handle_request(request)
```

### Advantages and Drawbacks
Advantages:
- Reduces coupling between senders of requests and receivers.
- Adds flexibility in assigning responsibilities to objects.

Drawbacks:
- Receipt of the request is not guaranteed.
- Can be hard to debug if the chain is not well-designed.

## Command

### Description
The Command pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

### When to Use
- When you want to parameterize objects with an action to perform.
- When you want to queue, specify, and execute requests at different times.
- When you need to support undo operations.

### Key Components
- Command: Declares an interface for executing an operation.
- ConcreteCommand: Defines a binding between a Receiver object and an action.
- Client: Creates a ConcreteCommand object and sets its receiver.
- Invoker: Asks the command to carry out the request.
- Receiver: Knows how to perform the operations associated with carrying out a request.

### Python Example

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()

remote.set_command(light_on)
remote.press_button()

remote.set_command(light_off)
remote.press_button()
```

### Advantages and Drawbacks
Advantages:
- Decouples the object that invokes the operation from the object that knows how to perform it.
- Easy to add new commands without changing existing code.

Drawbacks:
- Can lead to a large number of small command classes.

## Interpreter

### Description
The Interpreter pattern defines a representation for a grammar of a given language along with an interpreter that uses this representation to interpret sentences in the language.

### When to Use
- When you have a simple grammar to interpret.
- When efficiency is not a critical concern.

### Key Components
- AbstractExpression: Declares an abstract Interpret operation.
- TerminalExpression: Implements an Interpret operation associated with terminal symbols in the grammar.
- NonterminalExpression: Implements an Interpret operation for nonterminal symbols in the grammar.
- Context: Contains information that's global to the interpreter.
- Client: Builds (or is given) an abstract syntax tree representing a particular sentence in the language.

### Python Example

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        if self.data in context:
            return True
        return False

class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Usage
context = "John"

john = TerminalExpression("John")
henry = TerminalExpression("Henry")
mary = TerminalExpression("Mary")

is_male = OrExpression(john, henry)
is_mary = AndExpression(mary, Expression())

print(f"Is John male? {is_male.interpret(context)}")
print(f"Is Mary female? {is_mary.interpret(context)}")
```

### Advantages and Drawbacks
Advantages:
- Easy to change and extend the grammar.
- Implementing the grammar is straightforward.

Drawbacks:
- Complex grammars are hard to maintain.
- Can be inefficient for complex grammars.

## Iterator

### Description
The Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

### When to Use
- When you want to access an aggregate object's contents without exposing its internal representation.
- When you want to support multiple traversals of aggregate objects.
- When you want to provide a uniform interface for traversing different aggregate structures.

### Key Components
- Iterator: Defines an interface for accessing and traversing elements.
- ConcreteIterator: Implements the Iterator interface and keeps track of the current position in the traversal.
- Aggregate: Defines an interface for creating an Iterator object.
- ConcreteAggregate: Implements the Aggregate interface and returns an instance of the proper ConcreteIterator.

### Python Example

```python
from collections.abc import Iterable, Iterator

class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection, reverse=False):
        self._collection = sorted(collection)
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self):
        self._collection = []

    def __iter__(self):
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)

# Usage
collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
for item in collection:
    print(item)

print("\nReverse traversal:")
for item in collection.get_reverse_iterator():
    print(item)
```

### Advantages and Drawbacks
Advantages:
- Simplifies the interface of aggregate classes.
- Supports variations in the traversal of an aggregate.

Drawbacks:
- Applying the pattern to a simple collection may be an overkill.

## Mediator

### Description
The Mediator pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly, allowing you to vary their interaction independently.

### When to Use
- When a set of objects communicate in well-defined but complex ways.
- When reusing an object is difficult because it refers to and communicates with many other objects.

### Key Components
- Mediator: Defines an interface for communicating with Colleague objects.
- ConcreteMediator: Implements cooperative behavior by coordinating Colleague objects.
- Colleague: Each Colleague class knows its Mediator object and communicates with its mediator whenever it would have otherwise communicated with another colleague.

### Python Example

```python
from abc import ABC

class Mediator(ABC):
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

# Usage
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\nClient triggers operation D.")
c2.do_d()
```

### Advantages and Drawbacks
Advantages:
- Reduces coupling between components of a program.
- Centralizes control.
- Simplifies object protocols.

Drawbacks:
- Can become a "god object" (an object that knows too much or does too much).

## Memento

### Description
The Memento pattern captures and externalizes an object's internal state so that the object can be restored to this state later, without violating encapsulation.

### When to Use
- When you need to create snapshots of an object's state to be able to restore the object to its previous state.
- When direct access to the object's internal state would violate its encapsulation.

### Key Components
- Originator: Creates a memento containing a snapshot of its current internal state and uses the memento to restore its internal state.
- Memento: Stores internal state of the Originator object. The memento may store as much or as little of the originator's internal state as necessary at its originator's discretion.
- Caretaker: Responsible for the memento's safekeeping. Never operates on or examines the contents of a memento.

### Python Example

```python
from __future__ import annotations
from typing import List

class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

class Originator:
    _state = ""

    def set_state(self, state: str) -> None:
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save(self) -> Memento:
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_state()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_state())

# Usage
originator = Originator()
caretaker = Caretaker(originator)

originator.set_state("State #1")
originator.set_state("State #2")
caretaker.backup()

originator.set_state("State #3")
caretaker.backup()

originator.set_state("State #4")
print("\nCaretaker: Here's the current state:")
caretaker.show_history()

print("\nClient: Now, let's rollback!")
caretaker.undo()

print("\nClient: Once more!")
caretaker.undo()
```

### Advantages and Drawbacks
Advantages:
- Provides a way to implement undo/redo functionality.
- Doesn't violate encapsulation.

Drawbacks:
- Can be expensive in terms of memory if the originator's state is large and mementos are created frequently.

## Observer

### Description
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### When to Use
- When an abstraction has two aspects, one dependent on the other.
- When a change to one object requires changing others, and you don't know how many objects need to be changed.
- When an object should be able to notify other objects without making assumptions about who these objects are.

### Key Components
- Subject: Knows its observers and provides an interface for attaching and detaching Observer objects.
- Observer: Defines an updating interface for objects that should be notified of changes in a subject.
- ConcreteSubject: Stores state of interest to ConcreteObserver objects and sends a notification to its observers when its state changes.
- ConcreteObserver: Maintains a reference to a ConcreteSubject object, stores state that should stay consistent with the subject's, and implements the Observer updating interface to keep its state consistent with the subject's.

### Python Example

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self,observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    _state = None
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def some_business_logic(self):
        self._state = "New State"
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserverA(Observer):
    def update(self, state):
        print(f"ConcreteObserverA: Reacted to the event. New state: {state}")

class ConcreteObserverB(Observer):
    def update(self, state):
        print(f"ConcreteObserverB: Reacted to the event. New state: {state}")

# Usage
subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()
```

### Advantages and Drawbacks
Advantages:
- Supports the principle of loose coupling between objects that interact with each other.
- Allows sending data to other objects effectively without any change in the Subject or Observer classes.

Drawbacks:
- Observers are notified in random order.
- If not implemented carefully, it may cause memory leaks (subjects holding strong references to observers).

## State

### Description
The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

### When to Use
- When an object's behavior depends on its state, and it must change its behavior at runtime depending on that state.
- When operations have large, multipart conditional statements that depend on the object's state.

### Key Components
- Context: Defines the interface of interest to clients and maintains an instance of a ConcreteState subclass that defines the current state.
- State: Defines an interface for encapsulating the behavior associated with a particular state of the Context.
- ConcreteState subclasses: Each subclass implements a behavior associated with a state of the Context.

### Python Example

```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA handles the request.")
        return ConcreteStateB()

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB handles the request.")
        return ConcreteStateA()

class Context:
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state

    def request(self):
        self._state = self._state.handle()

# Usage
context = Context(ConcreteStateA())
context.request()
context.request()
context.request()
context.request()
```

### Advantages and Drawbacks
Advantages:
- Organizes the code related to particular states into separate classes.
- Makes state transitions explicit.
- Eliminates the need for large conditional statements.

Drawbacks:
- Can be overkill if a state machine has only a few states or rarely changes.

## Strategy

### Description
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it.

### When to Use
- When many related classes differ only in their behavior.
- When you need different variants of an algorithm.
- When an algorithm uses data that clients shouldn't know about.

### Key Components
- Context: Maintains a reference to a Strategy object and can be configured with a ConcreteStrategy object.
- Strategy: Declares an interface common to all supported algorithms.
- ConcreteStrategy: Implements the algorithm using the Strategy interface.

### Python Example

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b

class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Usage
context = Context(ConcreteStrategyAdd())
print(f"10 + 5 = {context.execute_strategy(10, 5)}")

context.set_strategy(ConcreteStrategySubtract())
print(f"10 - 5 = {context.execute_strategy(10, 5)}")

context.set_strategy(ConcreteStrategyMultiply())
print(f"10 * 5 = {context.execute_strategy(10, 5)}")
```

### Advantages and Drawbacks
Advantages:
- Provides a way to define a family of algorithms.
- Allows switching between algorithms at runtime.
- Reduces conditional statements in code.

Drawbacks:
- Clients must be aware of different strategies.
- Increases the number of objects in an application.

## Template Method

### Description
The Template Method pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

### When to Use
- When you want to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary.
- When common behavior among subclasses should be factored and localized in a common class to avoid code duplication.

### Key Components
- AbstractClass: Defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm and implements a template method defining the skeleton of an algorithm.
- ConcreteClass: Implements the primitive operations to carry out subclass-specific steps of the algorithm.

### Python Example

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("AbstractClass: I am doing the bulk of the work")

    def base_operation2(self):
        print("AbstractClass: But I let subclasses override some operations")

    def base_operation3(self):
        print("AbstractClass: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass

class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass1: Implemented Operation1")

    def required_operation2(self):
        print("ConcreteClass1: Implemented Operation2")

class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass2: Implemented Operation1")

    def required_operation2(self):
        print("ConcreteClass2: Implemented Operation2")

    def hook1(self):
        print("ConcreteClass2: Overridden Hook1")

# Usage
print("Same client code can work with different subclasses:")
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()

print("\n")

print("Same client code can work with different subclasses:")
concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
```

### Advantages and Drawbacks
Advantages:
- Reuses code among subclasses.
- Allows clients to override only certain parts of a large algorithm.

Drawbacks:
- Some clients may be limited by the provided skeleton of an algorithm.
- Might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.

## Visitor

### Description
The Visitor pattern represents an operation to be performed on the elements of an object structure. It lets you define a new operation without changing the classes of the elements on which it operates.

### When to Use
- When an object structure contains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes.
- When many distinct and unrelated operations need to be performed on objects in an object structure, and you want to avoid "polluting" their classes with these operations.

### Key Components
- Visitor: Declares a Visit operation for each class of ConcreteElement in the object structure.
- ConcreteVisitor: Implements each operation declared by Visitor.
- Element: Defines an Accept operation that takes a visitor as an argument.
- ConcreteElement: Implements an Accept operation that takes a visitor as an argument.
- ObjectStructure: Can enumerate its elements and may provide a high-level interface to allow the visitor to visit its elements.

### Python Example

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteComponentA(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self):
        return "A"

class ConcreteComponentB(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self):
        return "B"

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")

# Usage
components = [ConcreteComponentA(), ConcreteComponentB()]

print("The client code works with all visitors via the base Visitor interface:")
visitor1 = ConcreteVisitor1()
for component in components:
    component.accept(visitor1)

print("It allows the same client code to work with different types of visitors:")
visitor2 = ConcreteVisitor2()
for component in components:
    component.accept(visitor2)
```

### Advantages and Drawbacks
Advantages:
- Makes adding new operations easy.
- Gathers related operations and separates unrelated ones.

Drawbacks:
- Adding new ConcreteElement classes is hard.
- Can cause issues with encapsulation since the Visitor pattern assumes it can access relevant data in elements.

---

[Home](readme.md) | [Top](#behavioral-design-patterns)
