from ManejadorViajero import ManejadorViajero
from Menu import Menu


if __name__ == '__main__':
    manejador = ManejadorViajero("dataset.csv")
    listViajero = manejador.getViajeroList()

    menu = Menu()
    menu.getOpciones()
    opcionSelected = int(input("Ingresar una opcion: "))
    menu.opcion(opcionSelected, manejador)
