# [Design patterns](#design-patterns)
- [Design patterns](#design-patterns)
  - [Patterns structure](#patterns-structure)
  - [Short characteristics of each pattern](#short-characteristics-of-each-pattern)
    - [Creational patterns](#creational-patterns)
    - [Structural patterns](#structural-patterns)
    - [Behavioral patterns](#behavioral-patterns)

The patterns collected here are based on the classic book `Design Patterns: Elements of Reusable Object-Oriented Software` that provides a comprehensive overview of 23 different design patterns. The patterns are implemented in Python. The mentioned book is organized into three sections: [creational](patterns/creational/README.md), [structural](patterns/structural/README.md), and [behavioral](patterns/behavioral/README.md) patterns and the sample code will follow that organization structure.

## Patterns structure

The [creational](patterns/creational/README.md) patterns are:
- Abstract Factory
- Builder
- Factory Method
- Prototype
- Singleton

The [structural](patterns/structural/README.md) patterns are:
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

The [behavioral](patterns/behavioral/README.md) patterns are:
- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor


## Short characteristics of each pattern

### Creational patterns

- Abstract Factory: This pattern provides a way to create families of related or dependent objects without specifying their concrete classes. The factory is abstract and the concrete factories are its subclasses. The abstract factory provides an interface to create the objects, and the concrete factories implement this interface to create the actual objects. The objects created by the concrete factories are related in some way, such as they belong to the same family of objects. The Abstract Factory pattern is useful when a system must be independent of the way the objects it creates are generated, composed, and represented.

- Builder: This pattern separates the construction of a complex object from its representation so that the same construction process can create different representations. The builder pattern is used when the process of building a complex object is separate from the steps required to build the object. The builder abstracts the construction process and provides a set of methods that can be used to build the object step by step. The client uses the builder to specify the type of object it wants to build and then the builder builds the object.

- Factory Method: This pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. The Factory Method pattern is useful when a class cannot anticipate the type of objects it must create, or when a class wants its subclasses to specify the objects it creates. In this pattern, the superclass specifies the factory method, which returns an object of the type created by the factory. The subclasses then override this method to return an instance of the appropriate subclass.

- Prototype: This pattern allows an object to be cloned or copied to create new instances of the same type. The Prototype pattern is useful when creating a large number of instances of a class is time-consuming or resource-intensive. Instead of creating each instance from scratch, you can create a single instance and then use the prototype pattern to create additional instances as needed. The prototype pattern is also useful when you want to avoid defining a large number of classes that differ only slightly from each other.

- Singleton: This pattern restricts a class to have only one instance, while providing a global point of access to this instance. The Singleton pattern is useful when it is important to limit the number of instances of a class that can be created. It is also useful when you need to ensure that only one instance of a class exists, for example, to manage resources such as database connections. In the Singleton pattern, the class maintains a static instance of itself, and a static method provides access to this instance. The constructor of the class is private, which ensures that only one instance can be created.

### Structural patterns

- Adapter: This pattern allows objects with incompatible interfaces to work together by wrapping an object of one type in an adapter class that conforms to the interface required by the client. The adapter pattern is useful when you want to use an existing class, but its interface is not compatible with the class that you want to use it with. The adapter class implements the required interface and delegates calls to the existing class. The client communicates with the adapter, which in turn communicates with the existing class.

- Bridge: This pattern separates the abstraction from its implementation so that the two can vary independently. The bridge pattern is useful when you want to be able to change the implementation of a class without affecting the code that uses that class. The abstraction is an interface or abstract class, and the implementation is a concrete class that implements the abstraction. The abstraction delegates the calls it receives to the implementation, and the implementation performs the actual work.

- Composite: This pattern allows you to build complex objects from simple ones in a recursive manner. The composite pattern is useful when you want to represent part-whole hierarchies of objects, such as a tree structure. The composite pattern defines an abstract class or interface for the components, and concrete classes for the leaf nodes and composite nodes. The composite nodes contain a collection of components, which can be either leaf nodes or composite nodes. The client communicates with the components through the abstract class or interface, and the components handle the calls and pass them on to their children as needed.

- Decorator: This pattern allows you to add or extend the behavior of an object dynamically. The decorator pattern is useful when you want to add behavior to an object without changing its class, or when you want to add behavior to an object in a flexible way. The decorator pattern defines a decorator class that implements the same interface as the component class and contains a reference to a component object. The decorator class delegates the calls it receives to the component object, and can add additional behavior before or after the call to the component.

- Facade: This pattern provides a simplified interface to a complex system. The facade pattern is useful when you want to simplify the interface of a complex system so that it is easier to use. The facade class provides a simplified interface to the complex system, and delegates the calls it receives to the classes that make up the system. The client communicates with the system through the facade, which hides the complexity of the system and makes it easier to use.

- Flyweight: This pattern allows you to efficiently reuse a large number of similar objects. The flyweight pattern is useful when you have a large number of objects that share the same state, but each object has a unique identifier. The flyweight class defines the shared state and a factory class that creates and manages the flyweight objects. The client communicates with the flyweight objects through the flyweight class, and the flyweight objects share the same state.

- Proxy: This pattern provides a surrogate or placeholder object that controls access to an underlying object. The proxy pattern is useful when you want to control access to an object, or when you want to provide additional behavior to an object, such as caching or logging. The proxy class implements the same interface as the underlying object, and contains a reference to an instance of the underlying object. The client communicates with the proxy, which handles the calls and delegates them to the underlying object as needed. The proxy can add additional behavior to the calls it delegates to the underlying object, such as caching or logging. The proxy pattern provides a level of indirection, allowing you to modify the behavior of the underlying object without affecting the client that uses it.

### Behavioral patterns

- Chain of Responsibility: This pattern allows you to pass a request sequentially through a dynamic list of objects until one of them handles it. The chain of responsibility pattern is useful when you want to decouple the sender of a request from its receiver, and when you want to give multiple objects a chance to handle the request. The objects in the chain are linked together, and each object has a reference to the next object in the chain. When a request is made, it is passed to the first object in the chain, and if that object can't handle it, it is passed to the next object, and so on, until an object is found that can handle the request.

- Command: This pattern allows you to encapsulate a request as an object, thereby allowing you to pass requests as method calls, queue or log requests, and support undoable operations. The command pattern is useful when you want to decouple the sender of a request from its receiver, and when you want to pass requests as method calls, queue or log requests, and support undoable operations. The command class defines the request, and the concrete command classes implement the request by calling the appropriate methods on the receiver. The client creates the concrete command objects, and sets the receiver for each command object. The client also creates the invoker object, which holds the command objects and executes them.

- Interpreter: This pattern allows you to define a grammar for a simple language and then interpret sentences in that language. The interpreter pattern is useful when you have a language that you want to interpret, such as a mathematical expression or a script. The interpreter class defines the grammar for the language, and the concrete interpreter classes implement the grammar by evaluating sentences in the language. The client creates the concrete interpreter objects, and uses them to evaluate sentences in the language.

- Iterator: This pattern allows you to traverse a collection of objects without exposing the underlying representation of the collection. The iterator pattern is useful when you want to provide a standard way to access the elements of a collection, and when you want to decouple the collection from the code that uses it. The iterator class defines the interface for accessing the elements of a collection, and the concrete iterator classes implement the interface by accessing the elements of the underlying collection. The client uses the iterator class to traverse the elements of the collection, without having to know the underlying representation of the collection.

- Mediator: This pattern allows you to define a centralized communication system between objects, thereby reducing the coupling between the objects. The mediator pattern is useful when you have a large number of objects that communicate with each other, and you want to reduce the coupling between the objects. The mediator class defines the centralized communication system, and the concrete mediator classes implement the communication system by forwarding messages between the objects. The objects communicate with each other through the mediator, rather than directly, reducing the coupling between the objects.

- Memento: This pattern allows you to capture the internal state of an object, store it in a memento, and restore the state of the object later. The memento pattern is useful when you want to save the state of an object so that you can restore it later, and when you want to provide a way to undo operations. The memento class defines the internal state of an object, and the concrete memento classes implement the internal state. The originator class creates the memento objects, and the caretaker class stores the memento objects and restores the state of the originator when necessary. The memento pattern ensures that the internal state of the originator is not directly accessible by the caretaker, preserving the encapsulation of the originator.

- Observer: This pattern allows you to define a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically. The observer pattern is useful when you have a group of objects that need to be notified when another object changes state, and when you want to decouple the objects from one another. The subject class defines the one-to-many relationship between objects, and the concrete subject classes implement the relationship by maintaining a list of observer objects and notifying them when the subject changes state. The observer class defines the interface for receiving notifications from the subject, and the concrete observer classes implement the interface by updating themselves when they receive a notification from the subject.

- State: This pattern allows an object to alter its behavior when its internal state changes. The state pattern is useful when you have an object that can be in one of several states, and you want to encapsulate the behavior for each state in separate objects. The state class defines the interface for encapsulating the behavior for each state, and the concrete state classes implement the behavior for each state. The context class holds a reference to the current state object, and delegates requests to the current state object. When the internal state of the context changes, it changes the current state object to reflect the new state, and the behavior of the context changes accordingly.

- Strategy: This pattern allows you to define a family of algorithms, encapsulate each one as an object, and make them interchangeable. The strategy pattern is useful when you have a group of similar algorithms, and you want to choose the appropriate algorithm at runtime based on the context. The strategy class defines the interface for the algorithms, and the concrete strategy classes implement the algorithms. The context class holds a reference to a strategy object, and delegates requests to the strategy object. The client creates the context and the strategy objects, and sets the strategy for the context. The behavior of the context changes depending on the strategy that it uses.

- Template Method: This pattern allows you to define a skeleton algorithm, deferring some steps to subclasses. The template method pattern is useful when you have a common algorithm that can be divided into several steps, and some of the steps can be implemented differently by subclasses. The abstract class defines the template method, which contains the skeleton of the algorithm, and the concrete classes implement the algorithm by defining the missing steps. The client uses the concrete classes, and the behavior of the algorithm changes depending on the concrete class that is used.

- Visitor: This pattern allows you to define a new operation on objects without changing their classes. The visitor pattern is useful when you have a group of objects with similar structures, and you want to perform a new operation on the objects without changing their classes. The visitor class defines the new operation, and the concrete visitor classes implement the operation by visiting each object in the group and performing the operation. The objects in the group define an accept method, which accepts the visitor and calls the appropriate method on the visitor. The client creates the visitor and the objects in the group, and uses the visitor to perform the new operation on the objects.
