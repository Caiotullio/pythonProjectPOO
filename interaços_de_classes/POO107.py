from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever

escritor = Escritor('Joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()