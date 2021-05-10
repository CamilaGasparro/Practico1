 
import csv
from Proyecto import Proyecto

class ManejadorProyecto: 
    __nameFile = " "
    __listFile = []

    def __init__(self, nameFile = '0'):
        if nameFile != '0':
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file, delimiter = ";")

            for fila in reader:
                unProyecto = Proyecto(fila[0],fila[1],fila[2])
                self.__listFile.append(unProyecto)
            file.close()
        else:
            print("El nombre del archivo es invalido o el archivo no existe")

    def getFileList(self):
        return self.__listFile