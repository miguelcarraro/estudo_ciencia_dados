def validar_float(valor):
    try:
        return float(valor)
    except ValueError:
        print("Entrada invalida, tente novamente")
        exit()

def validar_int(valor):
    try:
        return int(valor)
    except ValueError:
        print("Entrada invalida, digite um número inteiro valido")
        exit()