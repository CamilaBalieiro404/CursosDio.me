print('---------SISTEMA BANCARIO------')
nome = input('Digite seu nome: ')
print(f'Bem-vindo {nome} ao nosso sistema bancario!\n')

AGENCIA_PADRAO = "0001"
clientes = []
contas = []

while True:
    print('--- MENU PRINCIPAL ---')
    print('1. Cadastrar Cliente')
    print('2. Consultar Cliente')
    print('3. Criar Conta Corrente')
    print('4. Listar Contas')
    print('5. Sair')
    
    try:
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Por favor, digite um número inteiro válido.\n')
        continue

    if opcao == 1:
        print('\n--- Cadastrar Cliente ---')
        cpf_cliente = input('Digite o CPF do cliente (apenas números): ')

        if len(cpf_cliente) != 11 or not cpf_cliente.isdigit():
            print('CPF inválido! O CPF deve conter exatamente 11 dígitos numéricos.\n')
            continue

        if any(c['cpf'] == cpf_cliente for c in clientes):
            print('Erro: Já existe um cliente cadastrado com este CPF!\n')
            continue
        nome_cliente = input('Digite o nome do cliente: ')
        data_nascimento = input('Digite a data de nascimento do cliente (dd/mm/aaaa): ')
        endereco_cliente = input('Digite o endereço do cliente: ')

        clientes.append({
            'nome': nome_cliente,
            'data_nascimento': data_nascimento,
            'cpf': cpf_cliente,
            'endereco': endereco_cliente
        })

        print(f'\nCliente {nome_cliente} com CPF {cpf_cliente} cadastrado com sucesso!\n')

    elif opcao == 2:
        print('\n--- Consultar Cliente ---')
        if not clientes:
            print('Nenhum cliente cadastrado no sistema até o momento.\n')
            continue

        cpf_consulta = input('Digite o CPF do cliente que deseja consultar: ')

        cliente_encontrado = None
        for c in clientes:
            if c['cpf'] == cpf_consulta:
                cliente_encontrado = c
                break

        if cliente_encontrado:
            print('\n-----------------------------')
            print(f"Nome: {cliente_encontrado['nome']}")
            print(f"CPF: {cliente_encontrado['cpf']}")
            print(f"Nascimento: {cliente_encontrado['data_nascimento']}")
            print(f"Endereço: {cliente_encontrado['endereco']}")
            print('-----------------------------\n')
        else:
            print('Cliente não encontrado!\n')

    elif opcao == 3:
        print('\n--- Criar Conta Corrente ---')
        cpf_cliente = input('Digite o CPF do titular da conta: ')

        titular = None
        for c in clientes:
            if c['cpf'] == cpf_cliente:
                titular = c
                break

        if not titular:
            print('Erro: Cliente não encontrado! Cadastre o cliente primeiro para abrir uma conta.\n')
            continue

        numero_conta = len(contas) + 1

        nova_conta = {
            'agencia': AGENCIA_PADRAO,
            'numero_conta': numero_conta,
            'usuario': titular
        }

        contas.append(nova_conta)
        print(f'\nConta criada com sucesso! Agência: {AGENCIA_PADRAO} | Conta: {numero_conta} | Titular: {titular["nome"]}\n')

    elif opcao == 4:
        print('\n--- Listar Contas Correntes ---')
        if not contas:
            print('Nenhuma conta cadastrada no sistema.\n')
            continue

        for conta in contas:
            print('-----------------------------------------')
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")
            print(f"CPF do Titular: {conta['usuario']['cpf']}")
            print('-----------------------------------------\n')

    elif opcao == 5:
        print('\nEncerrando o sistema... Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente.\n')