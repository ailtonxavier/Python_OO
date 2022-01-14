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

  def __pode_sacar(self, valor_do_saque):
    # verifica se o valor do saque é menor ou igual ao saldo mais o limite.
    return valor_do_saque <= self.__saldo + self.__limite

  def saque(self, valor):
    if self.__pode_sacar(valor):
      self.__saldo -= valor
    else:
      print("Você não tem limite suficiente.")

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

  @staticmethod
  def codigo_banco():
    return "001"

  @staticmethod
  def codigos_bancos():
    return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
