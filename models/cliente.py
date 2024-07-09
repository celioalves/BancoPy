from datetime import date, datetime
from utils.helper import str_p_date, date_para_str, formata_float_str_moeda


class Cliente:
    contador = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo = Cliente.contador
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento: date = str_p_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self):
        return date_para_str(self.__data_cadastro)

    def __str__(self):
        return (f'Código: {self.codigo} \nNome Cliente: {self.nome} '
                f'\nData de nascimento: {self.data_nascimento} \nData de cadastro: {self.data_cadastro}')

