class Pessoa:
    
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade    
    
p1 = Pessoa('Abimael',18)

print(p1.__dict__) #Ele mostra as informações contidas no objeto
#{'nome': 'Abimael', 'idade': 18} 
print(vars(p1)) #Ele mostra as informações contidas no objeto