from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente):
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1


    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor: float):
        self.__limite = valor

    @property
    def _calcula_saldo_total(self):
        return self.__saldo + self.__limite

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor: float):
        self.__saldo_total = valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Deposito efetuado com sucesso!')
        else:
            print('O valor precisa ser maior que 0. Tente novamente')

    def sacar(self, valor):
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso.')
        else:
            print('Saque não realizado. Tente novamente.')

    def transferir(self, destino: object, valor: float):
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total

            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso.')

        else:
            print('Transferência Não realizada. Tente Novamente')

    def __str__(self):
        return (f'Numero da conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo: {self.saldo}'
                f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}')
