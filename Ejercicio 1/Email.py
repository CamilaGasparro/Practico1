import re

PATTERN_PASS = re.compile("^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$")
PATTERN_EMAIL = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


class Email: #clase email
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __clave = ""

    def __init__(self, idCuenta="", dominio="", tipoDominio="", clave=""): #metodo constructor
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__clave = clave

    #metodo instanciables

    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, email):

        if(re.search(PATTERN_EMAIL, email)):
            halfEmail = email.split('@', 1)
            self.__tipoDominio = halfEmail[1].split('.')[0]
            self.__idCuenta = halfEmail[0]
            self.__dominio = halfEmail[1]

            matchPass = input("\t.Ingrese la clave: ")

            if(re.search(PATTERN_PASS, matchPass)):
                self.__clave = matchPass
                return True;
            else:
                print("\n < Clave no valida, intenta de nuevo > \n")
                return False;

        else:
            print("\n < Correo electronico invalido > \n")
            return False

    def changePassword(self):
        matchPass = input("\t.Ingresar clave actual: ")

        if(re.search(PATTERN_PASS, matchPass) and matchPass == self.__clave):

            newMatchPass = input("\t.Ingresar nueva clave: ")

            if(re.search(PATTERN_PASS, newMatchPass)):
                self.__clave = newMatchPass
                return True
            else:
                print("\n < Clave no valida, intenta de nuevo > \n")
                return False
        else:
            print("\n < Clave incorrecta, intenta de nuevo > \n")
            return False
