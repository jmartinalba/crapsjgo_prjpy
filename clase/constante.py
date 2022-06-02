from  pathlib import Path

class Constante:
    ''' En clase define las ruta completa de las figuras de los dados. Se
recupera la ruta del directorio de trabajo del usuario y se concatena con ruta
donde se localizan los archivos para almacenar, se crea una variable tipo diccionario  
almacenar cada una de las rutas.'''
    ARCHIVO_RUTA = str(Path.home()) + '/Programacion/crapsjgo_prjpy/src/img/'
    
    DICCIO_RUTA = {0 : ARCHIVO_RUTA + 'd0.png',
                   1 : ARCHIVO_RUTA + 'd1.png',
                   2 : ARCHIVO_RUTA + 'd2.png',
                   3 : ARCHIVO_RUTA + 'd3.png',
                   4 : ARCHIVO_RUTA + 'd4.png',
                   5 : ARCHIVO_RUTA + 'd5.png',
                   6 : ARCHIVO_RUTA + 'd6.png' }
    DICCIO_OBJT = {0 : 'imagend1', 1 : 'imagend2', 2: 'imagend3', 3 : 'imagend4'}

    VALOR_ANTERIOR = 0
    VALOR_CONTADOR = 1
