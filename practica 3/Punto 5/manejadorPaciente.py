from paciente import Paciente

class ManejadorPaciente():

    indice = 0
    __pacientes = None

    def __init__(self):
        self.__pacientes = []

    def agregarPaciente(self, paciente):
        paciente.rowid = ManejadorPaciente.indice
        ManejadorPaciente.indice+=1
        self.__pacientes.append(paciente)

    def getLista(self):
        return self.__pacientes
    
    def eliminarPaciente(self, paciente):
        indice = self.obtenerIndice(paciente)
        self.__pacientes.pop(indice)
    
    def actualizarPaciente(self, paciente):
        indice = self.obtenerIndice(paciente)
        self.__pacientes[indice] = paciente
    
    def obtenerIndice(self, paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+=1
        return i

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            pacientes = [paciente.toJSON() for paciente in self.__pacientes]
        )
        return d
