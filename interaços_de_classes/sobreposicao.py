class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando ...')


class Cliente(Pessoa):           #colocar o (Pessoa) faz a classe herda tudo que tem em class Pessoa
    def comprar(self):
        print(f'{self.nomeclasse} comprando ...')

    def falar(self):
        print('Estou em cliente')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')