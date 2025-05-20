class Pessoa:
    
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade    
    
p1 = Pessoa('Abimael',18)
print(p1.ano_nascimento())