from operacao import Operacao

class Subtracao(Operacao):
    simbolo = "-"
    nome = "Subtração"

    def calcular(self):
        return self.a - self.b