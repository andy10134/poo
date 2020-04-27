from ejemplo import Persona

if __name__ == '__main__':
    lista= []
    lista2= []

    lista.append(Persona('Mariana', '45666743'))

    lista2.append(Persona('Jorge','42356255'))
    lista2.append(Persona('Ana', '43488985'))

    lista.extend(lista2)

    print(lista2)

    lista2.pop()

    print(lista2)
