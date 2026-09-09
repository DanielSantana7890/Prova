from operacao import Operacao

class Divisao(Operacao):
    simbolo = "/"
    nome = "Divisao"

    def calcular(self):
        return self.a / self.b