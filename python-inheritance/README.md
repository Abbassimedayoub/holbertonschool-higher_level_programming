# Python - Inheritance
In Python, inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass) to inherit attributes and methods from another class (superclass). This enables code reuse, promotes modularity, and facilitates the creation of hierarchies of classes.

Here's a basic example of inheritance in Python:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog subclass inherits from Animal superclass
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog subclass
dog = Dog()

# Accessing methods from superclass and subclass
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
```

## In this example:

- Animal is the superclass, defining a method speak.
- Dog is the subclass, which inherits from Animal.
- Dog defines its own method bark.
- An instance of Dog can access both speak() from Animal and bark() from Dog.

## Here are some key points about inheritance in Python:
- Single Inheritance: Python supports single inheritance, where a subclass can inherit from only one superclass. However, a superclass can have multiple subclasses.

- Multiple Inheritance: Python also supports multiple inheritance, where a subclass can inherit from more than one superclass. This can be achieved by listing multiple base classes separated by commas in the class definition.

- Method Overriding: Subclasses can override methods inherited from their superclasses by providing a new implementation of the method with the same name.

- Method Resolution Order (MRO): In the case of multiple inheritance, Python uses the C3 linearization algorithm to determine the method resolution order, which determines the order in which methods are searched for and invoked.

- Access Control: In Python, access control to attributes and methods is not enforced by the language itself (like in some other languages such as Java). However, by convention, attributes and methods prefixed with a single underscore _ are considered private (though still accessible), while those prefixed with a double underscore __ are name-mangled to provide a degree of name privacy.

Inheritance is a powerful mechanism in Python that allows for code reuse, abstraction, and polymorphism, making it easier to create and maintain complex software systems. However, it should be used judiciously to maintain code clarity and simplicity.
