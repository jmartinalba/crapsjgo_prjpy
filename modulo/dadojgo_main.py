import sys
from  pathlib import Path
##sys.path.append(str(Path(__file__).parent.absolute()) + '/clase')
from clase.constante import Constante
from clase.dado import Dado
from modulo import guidado

''' De este módulo la función jugar() lleva control del juego, permanece en un
ciclo hasta el jugador pierda o gane el juego. '''

           
def jugar(builder):
       dado = Dado("JC")
       Constante.VALOR_CONTADOR = 1
       guidado.inicializaGui(builder)
       reglaUno(builder, dado)
       guidado.agregaRultadoToLabel(builder, dado)

       while(dado.edoJgo == "JC"):
           Constante.VALOR_CONTADOR  += 1
           reglaDos(builder, dado)
           guidado.agregaRultadoToLabel(builder, dado)
           guidado.agregaRultadoConsola(dado)

def reglaUno(builder, dado):
    dado.tirarDado()
    Constante.VALOR_ANTERIOR = dado.d1 + dado.d2
    dado.primerRegla()
    guidado.actualizaGui(builder, dado)       

def reglaDos(builder, dado):
       dado.tirarDado()
       dado.segundaRegla(Constante.VALOR_ANTERIOR)
       guidado.retardo(builder, dado)
       guidado.actualizaGui(builder, dado)

def inicializar(builder):
     guidado.inicializaGui(builder)
