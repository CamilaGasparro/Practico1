from Validation import Validation


class ViajeroFrecuente:
    __num_viajero = 0
    __DNI = 0
    __nombre = ' '
    __apellido = ' '
    __millasacumuladas = 0
    __valid = Validation()

    def __init__(self, num_viajero, dni, nombre, apellido, millas ):
        result = self.__valid.test({
            1: { 'data': num_viajero, 'type': int },
            2: { 'data': dni, 'type': int },
            3: { 'data': nombre, 'type': str },
            4: { 'data': apellido, 'type': str },
            5: { 'data': millas, 'type': int }
        })

        if result:
            self.__num_viajero= int(num_viajero)
            self.__DNI = int(dni)
            self.__nombre = str(nombre)
            self.__apellido = str(apellido)
            self.__millasacumuladas = int(millas)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.__num_viajero, self.__DNI, self.__nombre, self.__apellido, self.__millasacumuladas)

    def CantidadTotaldeMillas(self):
        return self.__millasacumuladas

    def setMillasAcumuladas(self, millasacumuladas):
            resu = self.__valid.test({
                1: {'data': millasacumuladas, 'type': int}
            })
            if resu:
                millas = int(millasacumuladas)

            if millasacumuladas > 0:
                self.__millasacumuladas = self.__millasacumuladas + millas
                print("Resultado de millas: " + str(self.__millasacumuladas))

    def canjearMillas(self,millas):
            res = self.__valid.test({
                1: {'data': millas, 'type': int}
            })
            if res:
                xmillas = int(millas)

            if self.__millasacumuladas > 0:
                self.__millasacumuladas = self.__millasacumuladas - xmillas
                print('Resultado de Millas:'+ str(self.__millasacumuladas))

    def getMillasAcumuladas(self):
        return self.__millasacumuladas

    def getNumeroViajero(self):
        return self.__num_viajero
