#from ManejadorMateria import ManejadorMateria
from ManejadorAlumnos import ManejadorAlumno

#Leer desde teclado un número de registro y mostrar Nombre del 
#alumno y dirección de correo. Nombre de las materias que está cursando,
#nombre de la/las correlativa y situación de la correlativa con el siguiente formato:

if __name__ == "__main__":
    materias = ManejadorMateria()
    alumnos = ManejadorAlumno()

    numero = int(input('Ingrese el numero de registro: '))

    alumno = alumnos.buscar_Alumno_porRegistro(numero)

    print('Alumno: ', alumno.get_nombre())
    print('Email: ', alumno.get_email())

    print('      Materia                          Correlativa                             Situación')



