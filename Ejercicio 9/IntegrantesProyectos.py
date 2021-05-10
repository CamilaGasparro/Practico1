
class IntegrantesProyectos:
    __idProyecto = " "
    __apellidoNombre = " "
    __dni = 0
    __categoriaInvestigacion = " "
    __rol = " "

    def __init__(self, id = " ", apenom = "", dni = '0', categoria = " ", rol = " "):
        self.__idProyecto = str(id)
        self.__apellidoNombre = str(apenom)
        self.__dni = int(dni)
        self.__categoriaInvestigacion = str(categoria)
        self.__rol = str(rol)

    def getIdProyecto(self):
        return self.__idProyecto

    def getApellidoNombre(self):
        return self.__apellidoNombre

    def getDni(self):
        return self.__dni

    def getCategoriaInvestigacion(self):
        return self.__categoriaInvestigacion

    def getRol(self):
        return self.__rol