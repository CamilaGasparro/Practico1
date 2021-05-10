
from ManejadorProyecto import ManejadorProyecto
from ManejadorIntegrantesProyecto  import ManejadorIntegrantesProyecto
from Menu import Menu

if __name__ == '__main__':

    proyecto = ManejadorProyecto("Proyectos.csv")
    integrantesProyecto = ManejadorIntegrantesProyecto("integrantesProyecto.csv")
    listIntegrantes = integrantesProyecto.getFileList()
    

    menu = Menu()
    menu.getOpciones()
    opcionSelected = int(input("Ingrese una opcion: "))
    menu.opcion(opcionSelected,listIntegrantes,integrantesProyecto) 
