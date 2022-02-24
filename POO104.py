'''
Public, protected, private
_ protected
__ private
'''
class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id,nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1, 'Otavio')
bd.inserir_clientes(2, 'Miranda')
bd.inserir_clientes(3, 'Rose')
bd.apaga_clientes(2)
bd.lista_clientes()
print(bd._dados)