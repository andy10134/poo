from ejemplo import Persona

if __name__ == '__main__':
    lista= []
    lista2= []

    lista.append(Persona('Mariana', '45666743'))

    print(lista)
    
    lista2.append(Persona('Jorge','42356255'))
    lista2.append(Persona('Ana', '43488985'))

    print("Lista2 =",lista2)

    lista.extend(lista2)

    print("Lista extendida por lista2 = ",lista)

    print("Vamos a ubicar a Mario en el indice 2")
    lista.insert(2, Persona('Mario', '21345627'))
    print(lista)

    lista.pop(2)
    print(lista)

    print("Lista con Mariana =", lista)
    lista.remove(Persona('Mariana','45666743'))
    print("Lista sin Mariana =",lista)

    lista.append(Persona('Ignacio','42564855'))

    lista.reverse()
    print('Lista invertida: ')
    print(lista)

    print("Lista sin orden =",lista)
    lista.sort()
    print("Lista orden Ascendente =",lista)
    lista.sort(reverse=True)
    print("Lista orden Descendente =",lista)

    lista2=lista.copy()
    print(lista2)

    lista2.clear()
    print(lista2)

