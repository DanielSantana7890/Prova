from operacao import Operacao

class Soma(Operacao):
    simbolo = "+"
    nome = "Somar"

    def calcular(self):
        return self.a + self.b