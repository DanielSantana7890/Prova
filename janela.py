import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multipli

OPERACOES = {
    "+": Soma,
    "-": Subtracao,
    "/": Divisao,
    "*": Multipli
}

ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")

        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False

        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignRight)

        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignRight)
        grade = QGridLayout()
        botoes = [
            ("c", 0, 0), ("<", 0, 1), ("+/-", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (",", 4, 1), ("=", 4, 2), 
        ]
        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            grade.addWidget(botao, linha, coluna, 1, largura)

            botao.clicked.connect(self.criar_acao(texto))
        
        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addWidget(self.visor)
        layout.addLayout(grade)
        self.setLayout(layout)


    def criar_acao(self, texto):

        return lambda: self.clicar(texto)
    
    def clicar(self, texto):

        if texto in "0123456789,":
            self.digitar(texto)
        elif texto in OPERACOES:
            self.escolher_operacao(texto)
        elif texto == "=":
            self.calcular()
        elif texto == "c":
            self.limpar()
        elif texto == "<":
            self.apagar()
        elif texto == "+/-":
            self.inverter_sinal()

    def digitar(self, tecla):

        if self.zerar:
            self.digitado = "0"
            self.zerar = False

        if tecla == ",":
            if "," not in self.digitado:
                self.digitado += ","
        else:
            if self.digitado == "0":
                self.digitado = tecla
            else:
                self.digitado += tecla

        self.visor.setText(self.digitado)

    def valor_do_visor(self):

        texto = self.digitado.replace(",", ".")
        return float(texto)

    def mostrar(self, numero):

        self.digitado = f"{numero:g}".replace(".", ",")
        self.visor.setText(self.digitado)
    
    def escolher_operacao(self, simbolo):

        if self.primeiro is not None and self.classe is not None and not self.zerar:
            self.calcular()

        self.primeiro = self.valor_do_visor()
        self.classe = OPERACOES[simbolo]
        self.simbolo = simbolo
        self.conta.setText(f"{self.digitado} {simbolo}")
        self.zerar = True

    def calcular(self):
        if self.primeiro is None or self.classe is None:
            return

        segundo = self.valor_do_visor()
        try:
            
            operacao = self.classe(self.primeiro, segundo)
            
            resultado = operacao.calcular() 
            
            self.conta.setText(f"{self.primeiro:g} {self.simbolo} {segundo:g} =".replace(".", ","))
            self.mostrar(resultado)
            
            self.primeiro = None
            self.classe = None
            self.zerar = True
        except ZeroDivisionError:
            self.visor.setText("Erro")
            self.limpar()

    def limpar(self):

        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.simbolo = ""
        self.zerar = False
        self.visor.setText("0")
        self.conta.setText("")

    def apagar(self):

        if len(self.digitado) > 1:
            self.digitado = self.digitado[:-1]
        else:
            self.digitado = "0"
        self.visor.setText(self.digitado)
        
    def inverter_sinal(self):
        valor = self.valor_do_visor()
        self.mostrar(-valor)

    

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()