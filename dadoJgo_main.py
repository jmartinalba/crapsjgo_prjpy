import sys
from  pathlib import Path
sys.path.append(str(Path(__file__).parent.absolute()) + '/clase')


from constante import Constante   # clase
from dado import Dado             # clase
from modulo import guiDado        # modulo
             
def jugar(builder):
       dado = Dado("JC")
       Constante.VALOR_CONTADOR = 1
       guiDado.inicializaGui(builder)
       reglaUno(builder, dado)
       guiDado.agregaRultadoToLabel(builder, dado)

       while(dado.edoJgo == "JC"):
           Constante.VALOR_CONTADOR  += 1
           reglaDos(builder, dado)
           guiDado.agregaRultadoToLabel(builder, dado)
           guiDado.agregaRultadoConsola(dado)

def reglaUno(builder, dado):
    dado.tirarDado()
    Constante.VALOR_ANTERIOR = dado.d1 + dado.d2
    dado.primerRegla()
    guiDado.actualizaGui(builder, dado)       

def reglaDos(builder, dado):
       dado.tirarDado()
       dado.segundaRegla(Constante.VALOR_ANTERIOR)
       guiDado.retardo(builder, dado)
       guiDado.actualizaGui(builder, dado)

def inicializar(builder):
     guiDado.inicializaGui(builder)
   


##When you call a method on a class (such as generatecode() in this case), Python automatically
##passes self as the first argument to the function. So when you call self.my_func(),
##it's more like calling MyClass.my_func(self). So when Python tells you "generatecode()
##takes 0 positional arguments but 1 was given", it's telling you that your method is set up to
##take no arguments, but the self argument is still being passed when the method is called,
##so in fact it is receiving one argument.
##
##Adding self to your method definition should resolve the problem.
##
##def generatecode(self):
##    pass  # Do stuff here
##
##Alternatively, you can make the method static, in which case Python will not pass self as the
##first argument:
##
##@staticmethod
##def generatecode():
##    pass  # Do stuff here




##The class attribute is always mistakingly considered to be the exact equivalent of the
##static attribute in Java or C++. To be accurate, class attributes in Python and static
##attributes in Java or C++ have a lot in common, however, they have behavioral
##differences that I will highlight in this article.


##An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object and it is defined inside the constructor function, __init__(self,..) of the class.
##
##    A class attribute is a Python variable that belongs to a class rather than a particular object. It is shared between all the objects of this class and it is defined outside the constructor function, __init__(self,...), of the class.        
    
        
        

   
