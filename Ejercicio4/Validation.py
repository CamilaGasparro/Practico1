import re


class Validation(object):
    #Aqui se pueden agregar todas las expresiones regulares que se necesite
    __regex = {
        'password': '^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$',
        'email': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    }

    def __init__(self):
        pass

    #Validaciond el tipo de dato determinado en la key "type" del diccionario
    def __test_data_type(self, key, dic):
        return True if type(dic[key]['type'](dic[key]['data'])) is dic[key]['type'] else False

    #Validaciones de la data con expresiones regulares
    def __test_regex(self, key, dic):
        if dic[key].get('regex') == None :
            return True

        elif self.__regex[dic[key]['regex']]:
            pattern = re.compile(self.__regex[dic[key]['regex']])
            return True if re.search(pattern, dic[key]['data']) else False

    #Funcion mapeadora de cada parametro enviado a validar
    def test(self, dic):
        for key in dic:
            if not self.__test_data_type(key, dic):
                print('\n < Data type error in -> {}: {} >'.format(key, dic[key]))
                return False

            if not self.__test_regex(key, dic):
                print('\n < Regular expression error in -> {}: {} >'.format(key, dic[key]))
                return False

        print('\n < Validations success >')
        return True


