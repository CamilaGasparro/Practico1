import csv
from Viajero import ViajeroFrecuente


class ManejadorViajero:
    __listFile = [] #lista con los viajeros almacenados desde el archivo
    __nameFile = "" #archivo con los viajeros

    def __init__(self, nameFile = ''):
        self.__getFileList(nameFile)

    def __getFileList(self, nameFile):
        if(nameFile != ""):
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file, delimiter = ',')

            for fila in reader:
                viajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listFile.append(viajero)

            file.close()
        else :
            print('\n<< Nombre invalido o archivo inexistente >>')

    def getViajeroList(self):
        return self.__listFile


    def findViajero(self, num_viajero):
        band = False
        index = 0

        while not band and index < len(self.__listFile):
            if(num_viajero == self.__listFile[index].getNumeroViajero()):
                band = True
            index+=1

        if band:
            return self.__listFile[index]
        else:
            return False
