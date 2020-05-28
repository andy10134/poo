from Inscripcion import Inscripcion
from TallerCapacitacion import TallerCapacitacion
from Persona import Persona
import numpy as np


class ManejadorInscripciones:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, cantidadInscripciones=20):
        self.__dimension = cantidadInscripciones
        self.__inscripciones = np.empty(self.__dimension, dtype=Inscripcion)

    def agregarInscripcion(self, persona, taller):
        if (type(taller) is TallerCapacitacion and type(persona) is Persona):
            if(self.buscarPersona):
                print("Se ha detectado una inscripcion en otro curso")
            else:
                if(self.__dimension == self.__cantidad):
                    self.__dimension += self.__incremento
                    self.__inscripciones.resize(self.__dimension)
                self.__inscripciones[self.__cantidad] = taller.agregarInscripcion(
                    Inscripcion(persona, taller)
                    )
                self.__cantidad += 1
                print('se inscribio una persona')
            else:
                print('no se logro inscribir la persona')

    def buscarPersona(self, dni, op=0):
        bandera = True
        i = 0
        while(bandera and i < self.__cantidad):
            if(type(self.__inscripciones[i]) is Inscripcion):
                persona = self.__inscripciones[i].getPersona()
                if(persona.getDni() == dni):
                    bandera = False
                else:
                    i += 1
            else:
                i += 1
        if(op):
            return (not bandera)
        if(not bandera):
            taller = self.__inscripciones[i].getTaller()
            print(
                'Esta persona se inscribió en el taller ' +
                taller.getNombre()
            )
            if(not self.__inscripciones[i].getPago()):
                print('Adeuda: {}'.format(taller.getMonto()))
            else:
                print('No adeuda el pago del taller')
        else:
            print('No se inscribió en ningún taller')

    def buscarTaller(self, id):
        for inscripcion in self.__inscripciones:
            if(type(inscripcion) is Inscripcion):
                taller = inscripcion.getTaller()
                if(taller.getId() == id):
                    persona = inscripcion.getPersona()
                    print('=====================')
                    print(persona)

    def toJSON(self):
        inscripciones = []
        for ins in self.__inscripciones:
            if(type(ins) is Inscripcion):
                inscripciones.append(ins.toJSON())
        d = dict(
            __class__=self.__class__.__name__,
            inscripciones=inscripciones
        )
        print(d)
        return d

    def cambiarPago(self, dni):
        bandera = True
        i = 0
        while(bandera and i < self.__cantidad):
            if(type(self.__inscripciones[i]) is Inscripcion):
                persona = self.__inscripciones[i].getPersona()
                if(persona.getDni() == dni):
                    bandera = False
                else:
                    i += 1
            else:
                i += 1
        if(not bandera):
            self.__inscripciones[i].setPago(True)
            print('Se registro el pago')
        else:
            print('No se inscribió en ningún taller')

    def mostrar(self):
        for ins in self.__inscripciones:
            print(ins)
