from herancasimples import Pessoa, Cliente, Aluno
from sobreposicao import Pessoa, Cliente, ClienteVIP

c1 = Cliente('Luiz', 45)
#c1.falar()       #usar em herança simples
c1.comprar()

print()

#a1 = Aluno('Maria', 54)
#a1.falar()
#a1.estudar()

c2 = ClienteVIP('Rose', 55, 'Costa')
c2.falar()