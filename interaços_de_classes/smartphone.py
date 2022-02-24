from herancamultipla import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} JA esta conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} Esta conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} Não esta conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desliado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False
