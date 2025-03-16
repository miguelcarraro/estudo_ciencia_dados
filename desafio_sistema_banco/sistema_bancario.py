menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("OPERAÇÃO DE DEPOSITO:")
        deposito = float(input("Quanto deseja depositar? "))
        if deposito > 0 :
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
        else:
            print("Digite um valor valido.")

    elif opcao == "s":
        print("OPERAÇÃO DE SAQUE:")
        saque = float(input("Quanto deseja sacar? "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saque:
            print("Você excedeu o limite de saques diários! \n Tente novamente amanha")

        elif excedeu_limite:
            print("O valor máximo para saque é de 500 reais")   

        elif excedeu_saldo:
            print("O valor solicitado é maior do que o seu saldo em conta.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido")

            
    elif opcao == "e":
        if not extrato:
           print("Não foram feitas nenhuma transação nos ultimos dias")
        else:
            print("EXTRATO:\n")  
            print(extrato)
            print(f"Saldo: R${saldo:.2f}")   

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")