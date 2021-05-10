
import os 
from ManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def getOpciones(self):
        os.system("cls")
        print("1.Calcular puntaje por proyecto\n2. Mostrar listado de los proyectos\n3. Salir")

    def opcion(self, op, listIntegrantes, integrantesProyecto):
        func = self.__switcher.get(op , lambda: print("Opcion invalida"))
        func(listIntegrantes, integrantesProyecto)

    def salir(self):
        print("Salir")

    def opcion1(self, listIntegrantes , integrantesProyecto):
        i= 0
        while i != '0':
            id = str(input(listIntegrantes[i].getIdProyecto()))
            pun = integrantesProyecto.calculoPuntaje(id)
            print("El puntaje del proyecto es: ", pun )
            i= i +1

    def opcion2(self, listIntegrantes, integrantesProyecto):
        pass 

    