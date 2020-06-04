# Narrativa          
# 
# De todo el personal se conoce la siguiente información: cuil, apellido, nombre, sueldo básico y antigüedad.
# 
# Si es un docente se registra además carrera en la que dicta clases, cargo y cátedra.
# 
# Si es personal de apoyo se registra además categoría.
# 
# Si es un investigador se registra además área de investigación y tipo de investigación
# 
# Si es un docente investigador se registra además carrera en la que dicta clases, cargo, cátedra, área de investigación y tipo de investigación, categoría en el programa de incentivos de investigación, importe extra por docencia e investigación.
# 
# Para cumplir con las tareas solicitadas por el analista, usted deberá:
# 
# a) Definir la jerarquía de clases correspondiente a la narrativa dada.
# 
# b) Almacenar en una colección tipo Lista definida por el programador, los agentes de la Universidad, obteniendo los datos del archivo “personal.json”, la misma deberá implementar la interfaz definida en el ejercicio 5. Los nodos de la lista, serán referencias a objetos que representen objetos de la clase base de la jerarquía.    
# 
# c) Implementar un programa principal con un menú de opciones que permita testear las siguientes acciones:
# 
#         Insertar a agentes a la colección.
#         Agregar agentes a la colección.
#          Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.
#         Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.
#          Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.
#         Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
#         Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.    
#         Almacenar los datos de todos los agentes en el archivo “personal.json”    
# 