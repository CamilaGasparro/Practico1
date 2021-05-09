from Validation import Validation


class Camion:
    __identificador = 0  
    __nombreConductor = " "
    __patenteCamion = " "
    __marcaCamion = " "
    __tara = 0
    __valid = Validation()

    def __init__(self, identificador, nombre, patente, marca, peso):
        result = self.__valid.test({
            1: {'data': identificador, 'type': int},
            2: {'data': nombre, 'type':str},
            3: {'data': patente, 'type':str},
            4: {'data': marca, 'type':str},
            5: {'data': peso, 'type': int}
        })

        if result:
            self.__identificador = int(identificador)
            self.__nombreConductor = str(nombre)
            self.__patenteCamion = str(patente)
            self.__marcaCamion = str(marca)
            self.__tara = int(peso)
  

    def __str__(self):
        return " {:>02}: {:<10}{:<8}{:<11}{:0000}.kg".format(self.__identificador,self.__nombreConductor, self.__patenteCamion,self.__marcaCamion, self.__tara)

    def getTara(self):
        return self.__tara
    
    def getId(self):
        return self.__identificador

    def getNombre(self):
        return self.__nombreConductor

    def getPatente(self):
        return self.__patenteCamion

 

    