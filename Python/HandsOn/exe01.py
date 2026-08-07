def sistema_bancario():
    saldo = 1000.0
    limite_saques = 3
    numero_saques = 0

    while True:
        print('*************Sistema Bancario**************')
        nome = input('Digite seu nome: ')
        print(f'Bem vindo {nome} ao nosso sistema bancario')     
        print('Escolha uma das opções abaixo:')
        print('1. Consultar saldo')
        print('2. Depositar')
        print('3. Sacar')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            print('Você escolheu consultar saldo')      
            print(f'Seu saldo atual é de R$ {saldo:.2f}')

        elif opcao == 2:
            print('Você escolheu depositar')      
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
            saldo += valor_deposito
            print(f'Você depositou R$ {valor_deposito:.2f} em sua conta.')
            print(f'Seu saldo atual é de R$ {saldo:.2f}')

        elif opcao == 3:
            print('Você escolheu sacar')
            
            # Verificação do limite de saques
            if numero_saques >= limite_saques:
                print('Operação falhou! Você atingiu o limite máximo de 3 saques.')
            else:
                valor_saque = float(input('Digite o valor que deseja sacar: '))
                
                # Opcional: verifica se há saldo suficiente
                if valor_saque > saldo:
                    print('Operação falhou! Você não tem saldo suficiente.')
                else:
                    saldo -= valor_saque
                    numero_saques += 1  # Incrementa a contagem de saques realizados
                    print(f'Você sacou R$ {valor_saque:.2f} de sua conta.')
                    print(f'Seu saldo atual é de R$ {saldo:.2f}')
                    print(f'Saques realizados hoje: {numero_saques}/{limite_saques}')

        else:
            print('Opção inválida!')

        print('\nDeseja realizar outra operação?')
        operacao = input('Digite S para sim ou N para não: ')
        
        if operacao.upper() == 'S':
            print('\nReiniciando o sistema...\n')
        else:
            print('Obrigado por utilizar nosso sistema bancário!')
            break
# Iniciar o programa
sistema_bancario()