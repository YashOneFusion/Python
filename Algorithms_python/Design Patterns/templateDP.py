#Create Abstract class
# Create template method
# Create overridable methods
from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):
    def template(self) -> None:
        self.base_operation()
        self.overridableFunc()

    def base_operation(self) -> None:
        print("Starting template operation\n")
    
    @abstractmethod
    def overridableFunc(self):
        pass


class ConvertToZIP(AbstractBaseClass):
    def overridableFunc(self):
        print("Converting the file to ZIP\n\n")
class ConvertToRAR(AbstractBaseClass):
    def overridableFunc(self):
        print("Converting the file to RAR\n\n")

def client(abstract_class: AbstractBaseClass) -> None:
    abstract_class.template()

client(ConvertToZIP())
client(ConvertToRAR())
