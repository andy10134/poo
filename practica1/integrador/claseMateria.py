class Materia:

    __RegistroA=0
    __Cod_materia=0
    __Nombre_Materia=""
    __Cod_correlativa=0
    __Nombre_correlativa=""
    __Estado_correlativa=""

    #error por que falta parametro por defecto en nombre correlativa
    def __init__(self,registro="" ,cod_materia=0 ,nombre_materia="",cod_correlativa=0,nombre_correlativa ='',estado_correlativa=""):
        
        self.__RegistroA = registro

        if( type(cod_materia) is int):
            self.__Cod_materia = cod_materia
        else: 
            print('Error en el dato codigo de materia')

        self.__Nombre_Materia = nombre_materia

        if( type(cod_correlativa) is int):
            self.__Cod_correlativa = cod_correlativa
        else: 
            print('Error en el dato codigo de correlativa')

        self.estado_correlativa = estado_correlativa

        if( type(nombre_correlativa) is str):
            self.__Nombre_correlativa = nombre_correlativa
        else:
            print('Error de tipo de dato en nombre de correlativa')
        

    def get_registro(self):
        return self.__RegistroA

    def get_cod_materia(self):

        return self.__Cod_materia

    def get_nombre_materia(self):

        return self.__Nombre_Materia

    #metodo duplicado
    #def get_nombre_materia(self):
    #
    #    return self.__Nombre_Materia

    def get_cod_correlativa(self):

        return self.__Cod_correlativa

    def get_nombre_correlativa(self):

        return self.__Nombre_correlativa

    def get_estado_correlativa(self):

        return self.__Estado_correlativa

    def mostrar(self):
        print('Nombre de la materia: ', self.get_nombre_materia())
        print('Nro de registro del alumno: ', self.get_registro())
        print('Codigo de la materia : ', self.get_cod_materia())
        print('Codigo de la correlativa: ', self.get_cod_correlativa())
        print('Nombre de la correlativa: ', self.get_nombre_correlativa())
        print('Estado de la correlativa', self.get_estado_correlativa())

