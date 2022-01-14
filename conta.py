class Conta:
  # def __init__ é a função construtora, toda classe necessariamente precisa ter uma função init
  def __init__(self, numero, titular, saldo, limite):
    print(f"Construindo objeto ... {self}")
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  def extrato(self):
    print(f"Saldo {self.__saldo} do titular {self.__titular}.")

  def deposito(self, valor):
    self.__saldo += valor

  def saque(self, valor):
    self.__saldo -= valor

  def transferencia(self, valor, destino):
    self.saque(valor)
    destino.deposito(valor)

  @property   # sintaxe para getter
  def saldo(self):
    return self.__saldo

  @property   # sintaxe para getter
  def titular(self):
    return self.__titular.title()

  @property   # sintaxe para getter
  def limite(self):
    return self.__limite

  @limite.setter  # sintaxe para setter
  def limite(self, limite):
    self.__limite = limite
