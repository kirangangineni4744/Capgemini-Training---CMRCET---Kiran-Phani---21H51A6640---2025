from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    
class Child(Father):
    def display(self):
        print("Child class")
        print("Defining abstract method")
        
class Relative(Father):
    def display(self):
        print("Relative class")
        print("Defining Relative method")

r=Relative()
c=Child()
c.display()
r.display()


