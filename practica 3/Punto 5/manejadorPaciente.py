from paciente import Paciente

class ManejadorPaciente():

    __pacientes = None

    def __init__(self):
        self.__paciente = []

    def agregarPaciente(self, paciente):
        self.__paciente.append(paciente)