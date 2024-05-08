import textwrap


def menu():
    menu = """\n
    ======= MENU  =========
        "[d] \tDepositar"
        "[s] \tSacar"
        "[e] \tExtrato"
        "[nc] \tNova Conta"
        "[lc] \tListar Conta"
        "[nu] \tNovo Usuário"
        "[q] \tSair Do Programa"
        "e\n"
        "===> """
    return input(textwrap.dedent(menu))


# Função para depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print('Depósito realizada com sucesso!')
    else:
        print('\nValor informado invalido.')
    return saldo, extrato


# Função para sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\nVoce nao tem saldo suficiente.')

    elif excedeu_limite:
        print('\nO valor do saldo excede o limite.')

    elif excedeu_saques:
        print('\nexcedeu a quantidade de saques permitido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizada com sucesso!')

    else:
        print('\nValor informado invalido.')
    return saldo, extrato

    print("Você selecionou a opção sacar.")


# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print('\n======== EXTRATO ==========')
    print('\nNao Foram Realizados movimentaçoes.' if not extrato else extrato)
    print(f'\nsaldo:\t\t R$ {saldo:.2f}')
    print(f'===========================')

    print("Você selecionou a opção exibir extrato.")


# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ')
    usuario_existente = filtrar_usuario(cpf, usuarios)

    if usuario_existente:
        print('Já existe usuário cadastrado com esse CPF!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe o data de nascimento: ')
    endereco = input('Informe o endereço completo: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('===== Usuário cadastrado com sucesso! =====')



# Função para filtrar usuário
def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else []



# Função para criar contas
def criar_contas(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do Usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n === Conta Criada com Sucesso! ===')
        conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}  # Define o usuário associado à conta
        return conta
    else:
        print('\nUsuário não cadastrado. Vamos criar um novo usuário.')
        criar_usuario(usuarios)  # Chama a função para criar um novo usuário
        novo_usuario = filtrar_usuario(cpf, usuarios)  # Filtra novamente o usuário recém-criado
        if novo_usuario:
            print('\n === Conta Criada com Sucesso! ===')
            conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': novo_usuario[0]}  # Define o usuário associado à conta
            return conta
        else:
            print('\nFalha ao criar o usuário. Operação encerrada.')
            return None  # Retorna None se falhar em criar o usuário e a conta



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']}
        C/conta:\t\t{conta['numero_conta']}
        Titular:\t\t{conta['usuario']['nome']}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor a do deposito: '))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == 's':
            valor = float(input('Digite o valor a do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)


        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_contas(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
