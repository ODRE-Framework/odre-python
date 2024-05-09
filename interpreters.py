from abc import ABC, abstractmethod

class Interpreter(ABC):

    @abstractmethod
    def transform(self, constraints_set):
        pass

    @abstractmethod
    def evaluate(self, expression):
        pass

    @abstractmethod
    def supports(self, action):
        pass
