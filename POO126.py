from dataclasse import dataclass

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __pos_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('B', '6')

pessoas = [p1, p2, p3,p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))

print(p1)
print(p1 == p2)

print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)


