#
# Autor: Michel
# Data: 22/01/2025

# criando as classe da lista 03
# 02
# importando a classe Animal
from animal import Animal

class Cachorro(Animal):
  def __init__(self, nome, idade, raca_cachorro):
    super().__init__(nome, idade)
    self.raca_cachorro = raca_cachorro

  def mostrar_detalhes(self):
    super().mostrarDetalhes()
    print(f"Raça do cachorro: {self.raca_cachorro}")

# analise do erro
# imprima o MRO da classe Cachorro
print(Cachorro.mro())
