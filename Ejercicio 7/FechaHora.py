
class FechaHora:
    __dia = 0 
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia = 1, mes = 1, año = 2021, hora = 0, min = 0, seg= 0):
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__año = int(año)
        self.__hora = int(hora)
        self.__minutos = int(min)
        self.__segundos = int(seg)

    def __VerificacionHora(self, seg, min, hor):
        totalMin = 0
        totalSeg = 0
        totalHora = 0

        if seg >= 60:
            min = min + int(seg / 60)
            totalSeg = seg - (int(seg / 60) * 60)
        else:
            totalSeg = seg

        if min >= 60:
            hor = hor + int(min / 60)
            totalMin = min - (int(min / 60) * 60)
        else: 
            totalMin = min

        if hor >= 24:
            totalHora = hor - (int(hor / 24) * 24)
        else: 
            totalHora = hor

        time = [totalSeg, totalMin, totalHora]
        return time   

    def __verificacionFecha(self, dia):

        #calendario
        diasMes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        #añobisiesto
        if(self.__año % 4 == 0) and ((self.__año % 100 != 0) or (self.__año % 400 == 0)): diasMes[2]= 29 
        mes = self.__mes
        año = self.__año

        #dia/mes/año
        if dia == 0 :
            mes = mes - 1
            if mes == 0:
                mes = 12
                año = año - 1
            dia = diasMes[mes]
        else: 
            while dia > diasMes[mes]:
                dia = dia - diasMes[mes]
                if mes != 12:
                    mes= mes + 1
                else: 
                    mes = 1
                    año = año + 1

        fecha = [dia, mes, año]
        return fecha

    def __add__(self, arg):
        resul = self.__VerificacionHora(self.__segundos + arg.getSegundos(), self.__minutos + arg.getMinutos(), self.__hora + arg.getHora())
        return FechaHora(self.__dia, self.__mes, self.__año, resul[2], resul[1], resul[0])
    
    def __radd__(self, arg):
        if str(arg).isdecimal():
            resul = self.__verificacionFecha(self.__dia + arg)
            return FechaHora(resul[0],resul[1],resul[2], self.__hora, self.__minutos, self.__segundos)
        else:
            resul = self.__VerificacionHora(self.__segundos + arg.getSegundos(), self.__minutos + arg.getMinutos(), self.__hora + arg.getHora())
            return FechaHora(self.__dia, self.__mes, self.__año, resul[2],resul[1],resul[0])      

    def __sub__(self, arg):
        resul = self.__verificacionFecha(self.__dia - arg)
        return FechaHora(resul[0], resul[1], resul[2], self.__hora, self.__minutos, self.__segundos)

    def Mostrar(self):
        return print(" {:02d}/{:02d}/{:4d} - {:02d}:{:02d}:{:02d}".format(self.__dia, self.__mes, self.__año, self.__hora, self.__minutos, self.__segundos))

    def ponerEnHora(self, hora = 0, min = 0, seg = 0):
        if hora > 0:
            self.__hora = hora
        if min > 0:
            self.__minutos = min
        if seg > 0:
            self.__segundos = seg
    

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAño(self):
        return self.__año

    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__minutos

    def getSegundos(self):
        return self.__segundos