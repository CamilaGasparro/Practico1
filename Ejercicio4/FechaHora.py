from Validation import Validation

class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    __valid = Validation()

    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, minutos = 0, segundos = 0):
        result = self.__valid.test({
            1:{'data': dia, 'type':int},
            2:{'data': mes, 'type':int},
            3:{'data': año, 'type':int},
            4:{'data': hora, 'type':int},
            5:{'data': minutos, 'type':int},
            6:{'data': segundos, 'type':int}
        })

        if result:
            self.__dia = int(dia)
            self.__mes = int(mes)
            self.__año = int(año)
            self.__hora = int(hora)
            self.__minutos = int(minutos)
            self.__segundos = int(segundos)

    def Mostrar(self):
        print(" {:02d}/{:02d}/{:4d} - {:02d}:{:02d}:{:02d} ".format(self.__dia, self.__mes, self.__año,self.__hora, self.__minutos, self.__segundos))

    def PonerEnHora(self, hora = 0, minutos = 0 , segundos = 0):
        res = self.__valid.test({
            1:{'data': hora, 'type':int},
            2:{'data': minutos, 'type':int},
            3:{'data': segundos, 'type':int}
        })

        if res:
            self.__hora = hora
            self.__minutos = minutos
            self.__segundos = segundos

    def AdelantarHora(self, hora = 0, minutos = 0, segundos = 0):

        resu = self.__valid.test({
            1:{'data': hora, 'type':int},
            2:{'data': minutos, 'type':int},
            3:{'data': segundos, 'type':int}
        })

        if resu:
            segundos = segundos + self.__segundos
            minutos = minutos + self.__minutos
            hora = hora + self.__hora

        #segundos
        if segundos >= 0:
            if segundos >= 60:
                self.__segundos = segundos - (int(segundos/60)*60)
                minutos = minutos + int(seg/60)
            else:
                self.__segundos = segundos

        #minutos
        if minutos >= 0:
            if minutos >= 60:
                self.__minutos = minutos - (int(minutos/60)*60)
                hora = hora + int(minutos/60)
            else:
                self.__minutos = minutos

        #horas
        if hora >= 0:
            if hora >= 24:
                self.__hora = hora - (int(hora/24)*24)
                self.__dia = self.__dia + int(hora/24)
            else:
                self.__hora = hora

        #calendario
        diasMes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        #añobisiesto
        if(self.__año % 4 == 0 ) and ((self.__año % 100 != 0) or (self.__año % 400 !=0)) : diasMes[2] = 29

        #dia/mes/año
        while self.__dia > diasMes[self.__mes]:
            self.__dia = self.__dia - diasMes[self.__mes]

            if self.__mes != 12:
                self.__mes = self.__mes + 1
            else:
                self.__mes = 1
                self.__año = self.__año + 1


