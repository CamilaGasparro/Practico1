import os
from Camion import Camion
from Cosecha import Cosecha

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
        print("1. Mostrar cantidad de kilos descargados\n2. Mostrar Listado de un dia\n3. Salir")

    def opcion(self, op, listCamion, listCosecha):
        func = self.__switcher.get(op, lambda: print("Opcion invalida"))
        func(listCamion, listCosecha)

    def salir(self):
        print("Salir")

    def opcion1(self, listCamion, listCosecha):
        idCamion = int(input("Ingrese numero de identificador de un camion "))
        kilos = 0
        if idCamion < len(listCamion) and idCamion > 0 :
            for i in range(len(listCosecha[idCamion - 1])):
                kilos = kilos + listCosecha[idCamion - 1][i]

            print("Cantidad total de kilos descargados durante {} dias {}.kg".format(len(listCosecha[idCamion - 1]), kilos))
        else:
            print("Identificador inexistente")



    def opcion2(self, listCamion, listCosecha):
        dia = int(input("Ingrese numero de un dia: "))
        if dia < len(listCosecha) and dia > 0:
            print(" {:<9}{:<11}{}\n ". format( 'PATENTE', "CONDUCTOR", "CANTIDAD DE KILOS"))

            for i in range(len(listCosecha)):
                print(" {:<9}{:<11}{:>4}.kg".format(listCamion[i].getPatente(), listCamion[i].getNombre(), listCosecha[i][dia - 1]))
        else:
            print("Dia inexistente")        
        