#from abc import ABCMeta,abstractmethod;
from abc import ABC,abstractmethod;
"""class shape(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        return 0;
"""
class shape(ABC):
    @abstractmethod
    def print(self):
        return 0;
class rectangle(shape):
    def __init__(self):
        self.length=12;
        self.breadth=13;
    def print(self):
        return self.length * self.breadth;
harry=rectangle();
print(harry.print());