#Create Abstract class
# Create template method
# Create overridable methods
from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):
    def template(self) -> None:
        self.base_operation()
        self.overridableFunc()

    def base_operation(self) -> None:
        print("Starting template operation")
    
    @abstractmethod
    def overridableFunc(self):
        pass


class ConcreteClass1(AbstractBaseClass):
    def overridableFunc(self):
        print("Fucntion Overriden in ConcClass 1")
class ConcreteClass2(AbstractBaseClass):
    def overridableFunc(self):
        print("Function overridden in ConcClass 2")

def client(abstract_class: AbstractBaseClass) -> None:
    abstract_class.template()

client(ConcreteClass1())
print("\n----------\n")
client(ConcreteClass2())
