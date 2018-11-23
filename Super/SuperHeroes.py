class  Persona():
    '''
    Clase para crear persona
    '''

    def __init__(self,nombre, estatura,peso,nacionalidad):
        '''Constructor de persona'''
        self.nombre=nombre
        self,estatura=estatura
        self.peso =peso
        self.nacionalidad = nacionalidad


class SuperPersonas(Persona):
    '''
    Clase para crear super personas
    '''
    def __init__(self,poderes = [],apodos =[]):
        '''Constructor de Super persona'''

        self.poderes=poderes
        self.apodos = apodos

    def actuar (self,ciudad):

        pass
    def hijos(self,padre,madre):
        pComunes=[]
        for pp in padre.poderes:
            if pp in madre.poderes:
                pComunes.append(pp)


class SuperHeroe(SuperPersonas):
    '''
    Clase para poder crear super Heroes
    '''

    def actuar(self, ciudad):
        print(self.apodos.pop() + 'Salva la ciudad de ' + ciudad)

class SuperVillano(SuperPersonas):
    '''
    Clase para poder crear super villanos
    '''
    def __init__(self,coste):
        self.coste=coste
    def actuar(self,ciudad):
        print(self.apodos.pop() + 'Ataca la ciudad de ' + ciudad)