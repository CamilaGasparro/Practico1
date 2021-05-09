from ManejadorCamion import ManejadorCamion
from Cosecha import Cosecha
from Menu import Menu

if __name__ == '__main__':

    dias = int(input("Cantidad de dias a evaluar: "))
    manejador = ManejadorCamion("archivoCamion.csv") 
    cosecha = Cosecha('archivoCosecha.csv', manejador.getFileList(), len(manejador.getFileList()), dias)

    menu = Menu()
    menu.getOpciones()
    opcionSelected = int(input("Ingresar una opcion: "))
    menu.opcion(opcionSelected, manejador.getFileList(), cosecha.getFileList())