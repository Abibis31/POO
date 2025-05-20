import json
CAMINHO_ARQUIVO='1.5.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

p1= Pessoa('Joao', 33)
p2= Pessoa('Maria', 20)      

bd=[vars(p1),vars(p2)]  

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)