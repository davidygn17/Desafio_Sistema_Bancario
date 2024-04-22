menu = """"


[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair 
e
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do deposito:R$  "))
        if valor > 0:
                 saldo += valor
                 extrato += f"R${valor:.2f}"

        else:
            print('operaçao invalida, informe um valor correto!')

    elif opcao == "s":
            valor = float(input("Digite o valor do Saque:R$  "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques > LIMITE_SAQUES

            if excedeu_saldo:
                print("Saldo insuficiente")
            elif excedeu_limite:
                print("Saldo insuficiente Excedeu limite de R$500 tente novamente")
            elif excedeu_saques:
                print("Limite de Saques excedeu")

            elif valor > 0:
                saldo -= valor
                extrato += f"R${valor:.2f}\n"
                numero_saques += 1
            else:
                print('Operação invalida, valor informado invalido')

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break

    else:
        print('Operação invalida, informe novamente a opçao Desejada!')