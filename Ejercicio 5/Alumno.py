from Validation import Validation

class Alumno:
    __nombre = ''
    __anio = 0
    __division = ''
    __inasistencias = 0
    maxInasistencias = 5
    cantClases = 25
    __valid = Validation()

    def __init__(self, nombre = '', anio = 0, division = '', inasistencias = 0):
        result = self.__valid.test({
            1: {'data': nombre, 'type':str},
            2: {'data': anio, 'type':int},
            3: {'data': division, 'type':str},
            4: {'data': inasistencias, 'type':int}
        })

        if result:
            self.__nombre = str(nombre)
            self.__anio = int(anio)
            self.__division = str(division)
            self.__inasistencias = int(inasistencias)
       

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__nombre, self.__anio, self.__division, self.__inasistencias)


    def getNombre(self):
        return self.__nombre

    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division

    def getInasistencias(self):
        return self.__inasistencias
        
    @classmethod
    def setMaxInasistencias(cls, xMaxInasistencias):
        resu = cls.__valid.test({
            1: {'data': xMaxInasistencias, 'type': int}
        })
        if resu: 
            maxInasistencias = int(xMaxInasistencias)
            cls.maxInasistencias = maxInasistencias


    @classmethod
    def getMaxInasistencias(cls):
        return cls.maxInasistencias
