from abc import ABC, abstractmethod

class Operacao(ABC):
    def __init__(self, a, b):
        self.__a = float(a)
        self.__b = float(b)
    
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    simbolo = None
    nome = None

    @abstractmethod
    def calcular(self):
        ...

    def __str__(self):
        return f"{self.a:g} {self.simbolo} {self.b:g} = {self.calcular():g}"