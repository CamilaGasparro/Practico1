
from FechaHora import FechaHora
import os 

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.salir
        }

    def switcher(self):
        return self.__switcher

    def getOpciones(self):
        os.system('cls')
        print("1. Sumar dos horas\n2. Restar dos horas\n3. Cual hora es mayor\n4. Salir")

    def opcion(self, op, fecha ):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func(fecha)
    
    def salir(self):
        print('salir')

    def opcion1(self, fecha):
        hora = int(input("\nHora 1\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg = int(input("Ingrese segundos: "))
        f1 = FechaHora()
        f1.ponerEnHora(hora, min, seg)

        hora = int(input("\nHora 2\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg= int(input("Ingrese segundos: "))
        f2 = FechaHora()
        f2.ponerEnHora(hora, min, seg)

        print("\n Hora 1: ")
        f1.mostrar()
        print("\n Hora 2: ")
        f2.mostrar()
        f3 = f1 + f2
        print("\n Resultado de f1 + f2: ")
        f3.mostrar()
        input() 
        

    def opcion2(self, fecha):
        hora = int(input("\nHora 1\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg = int(input("Ingrese segundos: "))
        f1 = FechaHora()
        f1.ponerEnHora(hora, min, seg)

        hora = int(input("\nHora 2\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg = int(input("Ingrese segundos: "))
        f2 = FechaHora()
        f2.ponerEnHora(hora, min, seg)

        print("\nHora 1: ")
        f1.mostrar()
        print("\nHora 2: ")
        f2.mostrar()
        f3 = f1 - f2
        print("\n Resultado de f1 - f2: ")
        f3.mostrar()
        input()

    def opcion3(self, fecha):
        hora = int(input("\nHora 1\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg = int(input("Ingrese minutos: "))
        f1 = FechaHora()
        f1.ponerEnHora(hora, min, seg)

        hora = int(input("\nHora 2\nIngrese hora: "))
        min = int(input("Ingrese minutos: "))
        seg = int(input("Ingrese minutos: "))
        f2 = FechaHora()
        f2.ponerEnHora(hora, min, seg)

        print("\nHora 1: ")
        f1.mostrar()
        print("\nHora 2: ")
        f2.mostrar()
        f3 = f1 > f2
        print("\n Resultado de f1 > f2: {} ".format(f3))
        input()
    
    
        







    

