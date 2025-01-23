#
# Autor: Michel
# Data: 22/01/2025

# criando as classe da lista 03
# 02
# importando a classe Animal
from animal import Animal

class Gato(Animal):
      def __init__(self, nome, idade, cor_pelagem):
            super().__init__(nome, idade)
            self.cor_pelagem = cor_pelagem

      def mostrar_detalhes(self):
            super().mostrar_detalhes()
            print(f"Cor da pelagem: {self.cor_pelagem}")
