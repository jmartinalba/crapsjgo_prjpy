import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from  pathlib import Path

sys.path.append(str(Path(__file__).parent.absolute()))

from modulo import dadojgo_main

class HandlerManejador:
    ''' Esta clase inicializa inicializa la interfaz gráfica
y asigna la función a la señales de los objetos Button. '''

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def on_button_jugar_clicked(self, button):
        dadojgo_main.jugar(builder)
    def on_button_continuar_clicked(self, button):
        dadojgo_main.inicializar(builder)
    def on_button_salir_clicked(self, button):
        sys.exit(0)
builder = Gtk.Builder()
builder.add_from_file("src/gladeGui/jgoDado.glade")
window = builder.get_object("ventana_main")
builder.connect_signals(HandlerManejador())
window.show_all()

Gtk.main()








