#
# Autor: Michel
# Data: 22/01/2025

# criando as classe da lista 03
# 01
class Animal:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def mostrarDetalhes(self):
    print(f"Nome:{self.nome}, Idade:{self.idade}")