
class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia = 1, mes = 1, año = 2021, hora = 0, minutos = 0, segundos = 0):
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__año = int(año)
        self.__hora = int(hora)
        self.__minutos = int(minutos)
        self.__segundos = int(segundos)

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
            hor = hor + int(seg / 60)
            totalMin = min - (int(min / 60) * 60)
        else: 
            totalMin = min

        if hor >= 24:
            totalHora = hor - (int(hor / 24) * 24)
        else: 
            totalHora = hor

        time = [totalSeg, totalMin, totalHora]
        return time

    def __add__(self, addFechaHora):
        resul = self.__VerificacionHora(self.__segundos + addFechaHora.getSegundos(), self.__minutos + addFechaHora.getMinutos(), self.__hora + addFechaHora.getHora())
        return FechaHora(self.__dia, self.__mes, self.__año, resul[2], resul[1], resul[0])
    
    def __sub__(self, addFechaHora):
        sub1 = self.__segundos - addFechaHora.getSegundos()
        sub2 = self.__minutos - addFechaHora.getMinutos()
        sub3 = self.__hora - addFechaHora.getHora()
        msub1 = int(((sub1 - 60) * -1) / 60)
        msub2 = int(((sub2 - 60) * -1) / 60)
        msub3 = int(((sub3 - 24) * -1) / 24)

        if sub1 < 0:
            sub1 = sub1 + 60 * msub1
        if sub1 * msub1 + 59 >= 60:
            sub2 = sub2 - msub1
        if sub2 < 0:
            sub2 = sub2 + 60 * msub2
        if sub2 * msub2 + 59 >= 60:
            sub3 = sub3 - msub2
        if sub3 < 0:
            sub3 = sub3 + 24 * msub3

        resul = self.__VerificacionHora(sub1, sub2, sub3)
        return FechaHora(self.__dia, self.__mes, self.__año, resul[2], resul[1], resul[0])
        
    def __gt__(self, addFechaHora):
        bandera = False

        if self.__hora > addFechaHora.getHora():
            bandera = True

        elif self.__hora == addFechaHora.getHora:
            if self.__minutos > addFechaHora.getMinutos():
                bandera = True

            elif self.__minutos == addFechaHora.getMinutos():
                if self.__seg > addFechaHora.getSegundos():
                    bandera = True
        
        return bandera

    def mostrar(self):
        return print("{:02d}/{:02d}/{:4d} - {:02d}:{:02d}:{:02d}".format(self.__dia, self.__mes, self.__año, self.__hora, self.__minutos, self.__segundos))

    def ponerEnHora(self, hor = 0, min = 0, seg = 0):
        if hor > 0:
            self.__hora = hor
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

    


