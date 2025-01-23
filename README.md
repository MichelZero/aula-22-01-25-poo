# aula-22-01-25-poo
aula-22-01-25-poo

correção no código da classe Passaro da aula do dia 22/01/2025

Corrigi o erro que aconteceu na classe de herança múltipla:

1.        Ao verificar o MRO da classe CachorroPassaro, verifiquei que a ordem de resolução ia para a classe Animal antes da classe Passaro (deixei o código usado para essa verificação, no fim do arquivo).

2.        Sendo assim causando o erro de argumento para a envergadura, que realmente não existe em animal.

3.        A solução foi, na segunda classe base remover a herança da classe Animal, assim a ordem de resolução fica correta em roda 100%.

4.        A única modificação que fiz foi na classe Passaro, deixei comentado onde modifiquei.

5.        Deixei o arquivo Classes para visualizar como fizemos em sala.
