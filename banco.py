from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main():
    menu()


def menu():
    print('=' * 40)
    print('=' * 13 + ' Bem-Vindo(a) ' + '=' * 13)
    print('=' * 11 + '  Banco  Python  ' + '=' * 12)
    print('=' * 40)

    print('Selecione uma opção no MENU: ')
    print('1 - CRIAR CONTA ')
    print('2 - EFETUAR SAQUE ')
    print('3 - EFETUAR DEPÓSITO ')
    print('4 - EFETUAR TRANSFERÊNCIA ')
    print('5 - LISTAR CONTAS ')
    print('6 - SAIR DO SISTEMA ')

    opcao: int = int(input())
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('O Banco Python agradece!')
        print('Volte sempre!')
        sleep(0.5)
        exit(0)
    else:
        print('opção inválida')
        sleep(1)
        menu()


def criar_conta():
    print('Informe os dados do Cliente ')
    nome: str = input('Informe o nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta:')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque():
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = int(input('Qual valor deseja sacar?'))
            conta.sacar(valor)
        else:
            print(f'Conta número {numero} não encontrada.')
    else:
        print('Não existem contas cadastradas')
    sleep(1)
    menu()


def efetuar_deposito():
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta para depósito: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = int(input('Qual valor deseja sacar?'))
            conta.depositar(valor)
        else:
            print(f'Conta número {numero} não encontrada.')
    else:
        print('Não existem contas cadastradas')
    sleep(1)
    menu()


def efetuar_transferencia():
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Digite a conta para qual deseja transferir'))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = int(input('Informe o valor a ser transferido: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'Conta número {numero_destino} não encontrada')
        else:
            print(f'Conta número {numero_origem} não encontrada.')
    else:
        print('Não existem contas cadastradas')
    sleep(1)
    menu()


def listar_contas():
    if len(contas) > 0:
        print('Listagem de contas')
        print('=' * 40)
        for conta in contas:
            print(conta)
            print('-' * 15)
            sleep(1)
    else:
        print('Não existem contas cadastradas até o momento')
    sleep(1)
    menu()


def listar_clientes():
    pass


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    else:
        return c
    sleep(1)
    menu()



if __name__ == '__main__':
    main()
