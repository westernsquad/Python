import random
class  Persona():
    '''
    Clase para crear persona
    '''

    def __init__(self,nombre,nacionalidad,estatura,peso):
        '''Constructor de persona'''
        self.nombre=nombre
        self.nacionalidad = nacionalidad
        self.estatura=estatura
        self.peso =peso



class SuperPersonas(Persona):
    '''
    Clase para crear super personas
    '''
    def __init__(self,nombre, nacionalidad,estatura,peso,poderes = [],apodos =[]):
        '''Constructor de Super persona'''
        super(SuperPersonas,self).__init__(nombre,nacionalidad,estatura,peso)
        self.poderes=poderes
        self.apodos = apodos

    def actuar (self,ciudad,verbo):
        a=self.apodos.pop()
        print (a,verbo,"la ciudad de " , ciudad)
        self.apodos.add(a)
    def hijos(self,pareja):
        nombre = self.nombre + pareja
        nacionalidad = self.nacionalidad + pareja
        estatura = self.estatura + pareja
        peso = self.peso + pareja
        poderes=set()
        u= self.poderes | pareja.poderes #es el conjunto de todos los poderes comunes
        try:
            for p in u:
                prob = 0
                if p in self.poderes and p in pareja.poderes:
                    prob=1
                if p in pareja:
                    prob+=0.5

                pf=prob/len(poderes)#max(len(poderes),1)#para evitar que sea 0
                if random.random() <= pf:
                    poderes.add(p)
        except ValueError:
            print("El hijo no tiene ningun poder")

        apodos=[]

        return (SuperPersonas(nombre,nacionalidad,estatura,peso,poderes,apodos))


class SuperHeroe(SuperPersonas):
    '''
    Clase para poder crear super Heroes
    '''

    def actuar(self, ciudad):
        super(SuperHeroe,self).actuar(ciudad,"salva")

class SuperVillano(SuperPersonas):
    '''
    Clase para poder crear super villanos
    '''
    def __init__(self,coste):
        self.coste=coste

    def actuar(self, ciudad):
        super(SuperHeroe, self).actuar(ciudad, "ataca")



p=Persona("pepe","ESP",1.8,75)
print(p.nombre)
p=SuperPersonas("pepe","Esp",1.8,75,["ivan la chupa","mucho"])
print(p.nombre)
print(p.poderes)
sh=SuperHeroe("pepe","Esp",1.8,75,["ivan la chupa","mucho"],["comepingas","gola"])
print(p.nombre)
print(sh.actuar("murcia"))