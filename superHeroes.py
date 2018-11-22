class SuperHeroe():
    '''
    classdocs
    '''

    def __init__(self, nombre, nacionalidad , estatura, peso, apodos= set(), poderes= []):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.apodos = apodos
        self.poderes = poderes
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.__peso = peso #los dos guiones son para variables privadas
        if len(self.apodos) < 1:
            self.apodos = {nombre}

    # Funciones de añadir y eliminar apodos, si se me queda vacio tiene que ser el nombre
    # Funcion que me pidan los apodos de un super heroe, pillar toda la lista de apodos y usar pop()

    def añadirApodo(self, apodo):
        self.apodos |= {apodo}
        #self.apodos = self.apodos.union({apodo})

    def eliminarApodo(self, apodo):
        self.apodos -= {apodo}
        if len (self.apodos)<1:
            self.apodos={self.nombre}

    def retirar (self):
        #for a in self.apodos:
            #self.apodos.remove(a)
        self.apodos= {self.nombre}

    def apodosSuper(self):
        self.apodos.pop()

    def añadirHeroes(self):
        l = []
        with open("SuperHeroes.txt", 'r') as f:
            for line in f:
                l.append(line)

    def exportHeroes1(self):
        with open("SuperHeroes.txt", 'w') as f:
            f.write("nombre: "+self.nombre + "\n")
            f.write("nacionalidad: "+self.nacionalidad+ "\n")
            f.write("estatura: "+self.estatura+ "\n")
            f.write("peso: "+self.__peso+ "\n")
            for p in self.poderes:
                f.write("apodos: "+self.poderes+ "\n")
            f.write("poderes: "+self.apodos+ "\n")
    def exportHeroes2(self):
        with open("SuperHeroes.txt", 'w') as f:
            f.write(self.nombre+"/")
            f.write(self.nacionalidad+"/")
            f.write(self.__peso+"/")
            for p in self.poderes:
                f.write(p+" ")
            f.write("/")
            for a in self.apodos:
                f.write(a+"")
            f.write("\n")

    def load1(self):
        with open("SuperHeroes.txt", "r")as f :
            line = f.readline()
            self.nombre = line.split(":")[1][1:]
            line = f.readline()
            self.nacionalidad = line.split(":")[1][1:]
            line = f.readline()
            self.estatura = line.split(":")[1][1:]
            line = f.readline()
            self.__peso = line.split(":")[1][1:]
            line = f.readline()
            self.poderes = line.split(":")[1].split()
            line = f.readline()
            self.apodos = set(line.split(":")[1].split())

    def load2(self):
        with open("SuperHeroes.txt","r") as f :
            line = f.readline()
            l=line.split("/")
            self.nombre=l[0]
            self.nacionalidad=l[1]
            self.estatura=l[2]
            self.__peso=l[3]
            self.poderes =l[4].split()
            self.apodos = set(l[5].split())


    def load3(self):
        with open("SuperHeroes.txt","r") as f :
            line = f.readline()#lee la version
            line =f.readline()
            l=line.split("/")
            self.nombre=l[0]
            self.nacionalidad=l[1]
            self.estatura=l[2]
            self.__peso=l[3]
            self.poderes =l[4].split()
            self.apodos = set(l[5].split())

    def load4(self):
        with open("SuperHeroes.txt","r") as f :
            self.nombre=f.readline()
            self.nacionalidad = f.readline()
            self.estatura = f.readline()
            self.__peso = f.readline()
            self.poderes = f.readline().split
            self.poderes = set(f.readline().split())




def noticia (superheroe):
    apodos = superheroe.apodos
    print('Se ha vuelto a ver a '+apodos.pop()+' en Nueva York, '+apodos.pop()+
          ' ha sido visto en Central Park,'+apodos.pop()+' gritaban los transeúntes.')



