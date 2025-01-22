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

#02
class Cachorro(Animal):
  def __init__(self, nome, idade, raca_cachorro):
    super().__init__(nome, idade)
    self.raca_cachorro = raca_cachorro

  def mostrar_detalhes(self):
    super().mostrar_detalhes()
    print(f"Raça do cachorro: {self.raca_cachorro}")

#03
class Gato(Animal):
  def __init__(self, nome, idade, cor_pelagem):
        super().__init__(nome, idade)
        self.cor_pelagem = cor_pelagem

  def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Cor da pelagem: {self.cor_pelagem}")
#04
class Passaro(Animal):
  def __init__(self, nome, idade, envergadura):
      super().__init__(nome, idade)
      self.envergadura = envergadura

  def mostrar_detalhes(self):
      super().mostrar_detalhes()
      print(f"Envergadura: {self.envergadura}")

#05
class CachorroPassaro(Cachorro, Passaro):
    def __init__(self, nome, idade, raca_cachorro, envergadura, caracteristicas_combinadas):
        Cachorro.__init__(self, nome, idade, raca_cachorro)
        Passaro.__init__(self, nome, idade, envergadura)
        self.caracteristicas_combinadas = caracteristicas_combinadas

    def mostrar_detalhes(self):
        Cachorro.mostrar_detalhes(self)
        Passaro.mostrar_detalhes(self)
        print(f"Características combinadas: {self.características_combinadas}")