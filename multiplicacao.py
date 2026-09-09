from operacao import Operacao

class Multipli(Operacao):
    simbolo = "*"
    nome = "multiplicacao"

    def calcular(self):
        return self.a * self.b