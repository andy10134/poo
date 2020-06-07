# Usar la narrativa del Ejercicio Nº 4
# 
# Se ha agregado nuevos requerimientos al sistema, y usted como programador, debe darles solución:
# 
# El sistema prevé que los empleados serán administrados a través de una colección. Existen dos interfaces distintas para operar con empleados, la interfaz del Tesorero, que solamente puede acceder a los gastos que la empresa tiene en concepto de sueldos, para ello, dado un número de documento, podrá consultar el gasto de sueldos para el empleado al que pertenece dicho número de documento.
# 
# La interfaz del Gerente, permite modificar el sueldo básico de un empleado de planta, el valor que se paga por hora de un empleado contratado o el valor que se paga por viático de un empleado externo; para ello debe proveerse el número de documento del empleado, y el valor que corresponda según lo que se quiera modificar.
# 
# Usted deberá crear las interfaces mencionadas con las funcionalidades solicitadas.
# 
# class ITesorero (Interface)
# 
#    def gastosSueldoPorEmpleado ( dni):
# 
#        pass
# 
#  
# 
# class IGerente (Interface)
# 
#    def modificarBasicoEPlanta(dni, nuevoBasico):
# 
#        pass
# 
#    def modificarViaticoEExterno(dni, nuevoViatico):
# 
#      pass
# 
#    def modificarValorEPorHora(dni, nuevoValorHora):
# 
#        pass
# 
# En el programa principal agregue una opción para el Tesorero y un menú de opciones para Gerente. Para ello deberá autenticar al usuario que quiere acceder, si es tesorero, accederá a las funcionalidades de tesorero y si es gerente, accederá a las funciones de gerente. La autenticación del usuario se hace pidiendo nombre de usuario y contraseña.
# 
# Usuario/contraseña para Tesorero: uTesoreso/ag@74ck
# 
# Usuario/contraseña para Gerente: uGerente/ufC77#!1