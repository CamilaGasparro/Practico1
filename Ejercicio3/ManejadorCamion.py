import csv
from Camion import Camion 

class ManejadorCamion:
    __listFile = [] #lista con los camiones almacenados desde el archivo
    __nameFile = " " #archivo con los camiones

    def __init__(self, nameFile = " "):
        if(nameFile != " "):
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file, delimiter = ',')

            for fila in reader: #por fila
                cam = Camion( fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listFile.append(cam)

            file.close()
        else:
            print('\n Nombre invalido o archivo inexistente')

    def getFileList(self):
        return self.__listFile
    


