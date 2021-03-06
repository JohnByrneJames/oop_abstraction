# Abstraction

# Abstraction is another concept of OOP wherein the user is kept unaware of basic implementation of a function
# property. The user is only able to view basic functionality whereas the internal details are hidden. The aim is to
# allow the user to know what they are doing but not how the work is being done. So for example, in an ATM the user
# just wants to access their money and carry out whatever they need to do, they do not care how the money is actually
# counted or how much money is in the machine. They are free to use the object has a whole.

# A common way to handle the complexity of a object is through something known as hierarchical abstraction.
from abc import ABC, abstractmethod


class AbsClass(ABC):  # subclass of ABC
    # normal method
    def print(self, x):
        print("Passed value : ", x)

    @abstractmethod
    def task(self):
        pass

class TestClass(AbsClass):  # subclass of AbsClass
    def task(self):
        print("We are inside test_class task")

class ExampleClass(AbsClass):  # subclass of AbsClass
    def task(self):
        print("We are inside example_class task")


# object of test_class created
testclass = TestClass()
testclass.task()
testclass.print(100)

#object of example_class created
exampleclass = ExampleClass()
exampleclass.task()
exampleclass.print(200)

# This will throw an error because the task method inside the AbsClass is an abstract method and cannot be made into
# an instance. It raises a TypeError: Can't instantiate abstract class AbsClass with abstract method task
# >>> tester = AbsClass()
# >>> tester.task()

print("test_obj is instance of Absclass? ", isinstance(testclass, AbsClass))  # True
print("example_obj is instance of Absclass? ", isinstance(exampleclass, AbsClass))  # True
