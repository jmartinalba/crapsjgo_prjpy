import secrets

class Dado:
    ''' Cuenta con tres propiedades de instancia y tres funciones que definen
su comportamiento '''
    def __init__(self, stringEdoJgo):
        self.edoJgo=stringEdoJgo
        self.d1=None
        self.d2=None

    def tirarDado(self):
        self.d1=1+secrets.randbelow(6)
        self.d2=1+secrets.randbelow(6)

    def primerRegla(self):
        if(self.d1+self.d2 == 7 or self.d1+self.d2 == 11):
            self.edoJgo = "JG"
        if(self.d1+self.d2==2 or self.d1+self.d2 == 3 or self.d1+self.d2 == 12):
            self.edoJgo = "JP"
    
    def segundaRegla(self, sumaAnterior):
        if(self.d1+self.d2 == 7):
            self.edoJgo = "JP"
        if(self.d1+self.d2 == sumaAnterior):
            self.edoJgo = "JG"
#________________________________________________________________________________
            
