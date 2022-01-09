class Conta:
  # def __init__ é a função construtora, toda classe necessariamente precisa ter uma função init
  def __init__(self, numero, titular, saldo, limite):
    print(f"Construindo objeto ... {self}")
    self.numero = numero
    self.titular = titular
    self.saldo = saldo
    self.limite = limite

  def extrato(self):
    print(f"Saldo {self.saldo} do titular {self.titular}.")

  def deposita(self, valor):
    self.saldo += valor

  def saque(self, valor):
    self.saldo -= valor