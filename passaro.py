# criando as classe da lista 03
# 02
# importando a classe Animal
from animal import Animal

class Passaro(Animal):
  def __init__(self, nome, idade, envergadura):
      super().__init__(nome, idade)
      self.envergadura = envergadura

  def mostrar_detalhes(self):
      super().mostrar_detalhes()
      print(f"Envergadura: {self.envergadura}")
