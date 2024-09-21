menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        #Verifica se o valor é menor do que 0
        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}"
        else:
            print(f"Operação falhou! O valor informado {valor} é inválido.")
    
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo o suficiente.")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += "fSaque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")
    
    elif opcao == "e":
        print("\n ===============Extrato===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n =====================================")


    elif opcao == "q":
        break
    else:
        print("Operaçãp inválida, por favor selecione a operação eu tenho treinar")
