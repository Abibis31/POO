import json

from AjsonPOO import CAMINHO_ARQUIVO, Pessoa

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    