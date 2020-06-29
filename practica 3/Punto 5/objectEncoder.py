import json
from pathlib import Path
from paciente import Paciente
from manejadorPaciente import ManejadorPaciente


class ObjectEncoder(object):

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
        destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if(class_name == 'ManejadorPaciente'):
                pacientes = d['pacientes']
                dPacientes = pacientes[0]
                manejador = class_()
                for i in range(len(pacientes)):
                    dPacientes = pacientes[i]
                    class_name = dPacientes.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPacientes['__atributos__']
                    unPaciente = class_(**atributos)
                    manejador.agregarPaciente(unPaciente)
            return manejador
