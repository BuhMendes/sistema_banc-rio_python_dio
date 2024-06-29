menu = """
    MENU

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depositar")
        valor_deposito = float (input("Informe o valor de despósito: "))
        if valor_deposito <= 0:
            print("Valor de deposito não é válido.")

        else:
            saldo += valor_deposito
            extrato += (f"\n Depósito: R$ {valor_deposito:.2f}")
            print("Depósito realizado!")
    

    elif opcao == "2":
        print("Sacar")
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido.")
        else: 
            valor_saque = float (input("Informe o valor para sacar: "))
                
            if valor_saque > limite:
                print("Valor maior que o limite de saque.")
            elif valor_saque > saldo:
                print("Não será possível sacar o dinheiro por falta de saldo.")
            elif valor_saque <= 0:
                print("Valor de saque não é válido.")
            else: 
                saldo -= valor_saque
                extrato += (f"\n Saque: R$ {valor_saque:.2f}")
                numero_saques += 1
                print("Saque realizado!")


    elif opcao == "3":
        print("Extrato")

        print(extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
   

    elif opcao == "0":
        break

    else:
        print("Operação inválida!")
