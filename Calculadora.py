from soma import Soma
from subtracao import Subtracao
OPCOES = {
    "1": Soma,
    "2": Subtracao

}
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",","."))
        except ValueError:
            print("Valor Invalido, digite um numero")

def ler_opcao():
    print("\n=== Calculadora ===")
    for chave, classe in OPCOES.items():
        print(f"{chave} - {classe.nome}")
    print("0 - Sair")

    while True:
        escolha = input("Escolha uma opções: ").strip()
        if escolha == "0" or escolha in OPCOES:
            return escolha
        print("Opção Invalida")

def main():
    while True:
        escolha = ler_opcao()
        if escolha == "0":
            print("Até mais")
            break

        a = ler_numero("Digite um Numero: ")
        b = ler_numero("Digite outro Numero: ")

        operacao = OPCOES[escolha](a,b)

        print(f"\nResultado: {operacao}")

if __name__ == "__main__":
    main()