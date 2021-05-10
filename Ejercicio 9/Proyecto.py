
class Proyecto: 
    __idProyecto = " "
    __titulo = " "
    __palabrasClave = " "

    def __init__(self, id = " ", titulo = " ", palabras = " "):
        self.__idProyecto = str(id)
        self.__titulo = str(titulo)
        self.__palabrasClave = str(palabras)

def getIdProyecto(self):
    return self.__idProyecto

def getTitulo(self):
    return self.__titulo

def getPalabrasClaves(self):
    return self.__palabrasClave
