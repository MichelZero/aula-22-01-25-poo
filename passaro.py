# criando as classe da lista 03
# 02
# importando a classe Animal
from animal import Animal

# passaro.py
class Passaro: # removi a herança de Animal
  def __init__(self, nome, idade, envergadura):
        self.nome = nome
        self.idade = idade
        self.envergadura = envergadura

  def mostrar_detalhes(self):
    # super().mostrar_detalhes() # removi pois a classe Passaro não herda de nenhuma outra classe
    print(f"Envergadura: {self.envergadura}")
    
