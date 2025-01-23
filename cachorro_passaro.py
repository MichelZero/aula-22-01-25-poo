# criando as classe da lista 03
# 02
# importando a classe Animal
from cachorro import Cachorro
from passaro import Passaro

class CachorroPassaro(Cachorro, Passaro):
    def __init__(self, nome, idade, raca_cachorro, envergadura, caracteristicas_combinadas):
        Cachorro.__init__(self, nome, idade, raca_cachorro)
        Passaro.__init__(self, nome, idade, envergadura)
        self.caracteristicas_combinadas = caracteristicas_combinadas
    

    def mostrar_detalhes(self):
        Cachorro.mostrar_detalhes(self)
        Passaro.mostrar_detalhes(self)
        print(f"Características combinadas: {self.caracteristicas_combinadas}")


# analise do erro
# imprima o MRO da classe CachorroPassaro
print(CachorroPassaro.mro())