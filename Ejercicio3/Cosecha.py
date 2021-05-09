import csv 

class Cosecha:
    __listFile = [] #lista bidimensional con la cantidad de kilos por dia 

    def __init__(self, nameFile = '0', listCamion = [], row = 0, col = 0):
        if nameFile != '0' and type(self.__listFile) == type(listCamion):
            self.__nameFile = nameFile
            file = open(nameFile)
            reader = csv.reader(file , delimiter = ',')
            i = 0 #para el archivo de camion 
            for row in reader:
                self.__listFile.append([])
                for j in range(col): #archivo de cosecha
                    self.__listFile[i].append(int(row[j]) - listCamion[i].getTara())
                i = i + 1

            file.close()
        else:
            print("Nombre invalido o archivo inexistente")

    def getFileList(self):
        return self.__listFile
            
