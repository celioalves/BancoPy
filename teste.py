from models.cliente import Cliente
from models.conta import Conta


sergio: Cliente = Cliente('Sérgio Guanabara', 'sergiog@gmail.com', '123.456.789-00',
                          '15/04/1980')

magda: Cliente = Cliente('Magda Salão Antibes', 'magda@saidebaixo.com.br', '987.654.321.01',
                         '21/10/1963')

ccs: Conta = Conta(sergio)
ccm: Conta = Conta(magda)

print(sergio)
print(ccs)
print('=' * 30)
print(magda)
print(ccm)

print('=' * 40)
print('=' * 13 + ' Bem-Vindo(a) ' + '=' * 13)
print('=' * 11 + '  Banco  Python  ' + '=' * 12)
print('=' * 40)
