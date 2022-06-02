import time
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from clase.constante import Constante

''' El módulo actualiza la interfaz gráfica,  es necesario events_pending() de
Gtk forzar que se actualice '''

def actualizaGui(builder, dado):
    img_d1 = builder.get_object(Constante.DICCIO_OBJT[0])
    img_d2 = builder.get_object(Constante.DICCIO_OBJT[1])
    img_d1.set_from_file(Constante.DICCIO_RUTA[dado.d1])
    img_d2.set_from_file(Constante.DICCIO_RUTA[dado.d2])

    labelSumaPrimera = builder.get_object("label_sumaPrimera")
    labelSumaActual = builder.get_object("label_sumaActual")
    labelEdoJgo = builder.get_object("label_edoJgo")
        
    labelSumaPrimera.set_label(str(Constante.VALOR_ANTERIOR))
    labelSumaActual.set_label(str(dado.d1 + dado.d2))
    labelEdoJgo.set_label(dado.edoJgo)

def inicializaGui(builder):

    img_d1 = builder.get_object(Constante.DICCIO_OBJT[0])
    img_d2 = builder.get_object(Constante.DICCIO_OBJT[1])
    img_d1.set_from_file(Constante.DICCIO_RUTA[0])
    img_d2.set_from_file(Constante.DICCIO_RUTA[0])
    
    labelSumaPrimera = builder.get_object("label_sumaPrimera")
    labelSumaActual = builder.get_object("label_sumaActual")
    labelEdoJgo = builder.get_object("label_edoJgo")

    labelResultado = builder.get_object("label_resultado")
    labelResultado.set_label("NoTir  D1  D2  Suma  EdoJgo" + "\n")

        
    labelSumaPrimera.set_label("0")
    labelSumaActual.set_label("0")
    labelEdoJgo.set_label("SG")

def agregaRultadoToLabel(builder, dado):
    strResultado = str(Constante.VALOR_CONTADOR) + "             " +  str(dado.d1) + "     " + str(dado.d2) + "     " + str(dado.d1 + dado.d2) + "            " + dado.edoJgo + "\n"
    labelResultado = builder.get_object("label_resultado")
    labelResultado.set_label(labelResultado.get_text() +  strResultado)


def agregaRultadoConsola(dado):
    strResultado = str(Constante.VALOR_CONTADOR) + "      " +  str(dado.d1) + "   " + str(dado.d2) + "   " + str(dado.d1 + dado.d2) + "     " + dado.edoJgo
    

def retardo(builder, dado):
    updateGUI()
    for i in range(3):
        time.sleep(0.3)


def updateGUI():
    ''' Force update of GTK mainloop during a long-running process '''
    while Gtk.events_pending():
        Gtk.main_iteration()  


        
        

   
