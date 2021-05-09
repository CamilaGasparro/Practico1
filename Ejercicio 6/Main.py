
from Menu import Menu
from FechaHora import FechaHora

if __name__ == '__main__': 

    fechaHora = FechaHora()
    menu = Menu()
    menu.getOpciones()
    opcionSelected = int(input("Ingrese una opcion: "))
    menu.opcion(opcionSelected, fechaHora)
