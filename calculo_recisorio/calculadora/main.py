from calculadora.recisao import calculo_recisao
from calculadora.utils import validar_float, validar_int

def main():
    print("Calculadora de Recisão de Contrato de Trabalho")

    salario = validar_float(input("Digite o salário do funcionário: R$"))
    meses_trabalhados = validar_int(input("Digite quantos meses o funcionário trabalhou: "))
    aviso_previo = input("O funcionário deu aviso prévio? (S/N): ").strip().lower()

    if aviso_previo == "s":
        aviso_previo = True
    elif aviso_previo == "n":
        aviso_previo = False
    else:
        print("Entrada invalida, digite 'S' para sim ou 'N' para não")
        exit()

    resultado = calculo_recisao(salario, meses_trabalhados, aviso_previo)

    print("\nDetalhamento da Recisão:")
    for chave, valor in resultado.items():
        print(f"{chave}: R${valor:.2f}")

if __name__ == "__main__":
    main()