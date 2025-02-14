# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
numeros =[1, 2, 3, 4, 5]
# Añade el número 6 al final usando append().
numeros.append(6)
# Inserta el número 10 en la posición 2 usando insert().
numeros.insert(2, 10)
# Modifica el primer elemento de la lista para que sea 0.
numeros[0] = 0

print(numeros)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend() para agregar elementos al final de la lista.
lista_a.extend(lista_b)
print(lista_a)
# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
elemento_eliminado = lista_a.pop(3)
print(elemento_eliminado)

# Limpia completamente lista_b usando clear().

lista_b.clear()