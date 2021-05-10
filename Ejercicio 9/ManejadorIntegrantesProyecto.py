
import csv
from IntegrantesProyectos import IntegrantesProyectos

class ManejadorIntegrantesProyecto:
    __nameFile = ' '
    __listFile = []

    def __init__(self, nameFile = '0'):
        if nameFile != '0':
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file, delimiter = ";")

            for fila in reader:
                unIntegrante = IntegrantesProyectos(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listFile.append(unIntegrante)
            file.close()
        else:
            print("El nombre del archivo es invalido o el archivo no existe")
            
    def getFileList(self):
        return self.__listFile

    def calculoPuntaje (self, id):
        i= 0
        puntaje = 0
        if id != "0":
    
            if ((self.__listFile[i].getRol() == "integrante") <= 3):
                puntaje = puntaje + 10

            else: 
                puntaje = puntaje - 20 
                print("El Proyecto debe tener como minimo tres integrantes")

            if (self.__listFile[i].getRol() == "director"):

                if ((self.__listFile[i].getCategoriaInvestigacion() == "I") or  (self.__listFile[i].getCategoriaInvestigacion() == "II")) :
                    puntaje = puntaje + 10

                else:
                    puntaje = puntaje - 5
                    print("El director del proyecto debe tener como minimo categoria I o II")   

            if (self.__listFile[i].getRol() == "codirector"):
                if ((self.__listFile[i].getCategoriaInvestigacion() == "I") or (self.__listFile[i].getCategoriaInvestigacion() == "II") or (self.__listFile[i].getCategoriaInvestigacion() == "III")):
                    puntaje = puntaje + 10
                else: 
                    puntaje = puntaje - 5
                    print("El codirector del proyecto debe tener como minimo categoria III")

            if self.__listFile[i].getRol() == "director":
                print("Tiene Director")

            else: 
                print("El proyecto debe tener un director")  
                puntaje = puntaje - 10

            if self.__listFile[i].getRol() == "codirector":
                print("Tiene un codirector")
             
            else:
                print("El proyecto debe tener un codirector")
                puntaje = puntaje - 10  
   
        else:
            print("El proyecto no existe")    
        return puntaje        





            
            

