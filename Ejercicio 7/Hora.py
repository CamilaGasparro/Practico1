
class Hora:
    __min = 0
    __seg = 0
    __hora = 0

    def __init__(self, hora = 0, min = 0, seg = 0):
        self.__hora = int(hora)
        self.__min = int(min)
        self.__seg = int(seg)

    def Mostrar(self):
        return print(" {:02d}:{:02d}:{:02d}".format(self.__hora, self.__min, self.__seg))
    
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

    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__min

    def getSegundos(self):
        return self.__seg