class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self,alimento):
        return f'{self.nome} está comendo'f' {alimento}'

leao = Animal('leao')
print(leao.nome)
print(leao.comendo('abacaxi'))            