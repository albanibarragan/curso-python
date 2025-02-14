# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numeros[2:5]
print(numeros)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
numeros_aleatorios = [5, 2, 8, 1, 9, 4, 2]
# Ordena la lista de forma ascendente usando sort().
numeros_aleatorios.sort()
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
print(numeros_aleatorios.count(2))
# Comprueba si el número 7 está en la lista usando in.
print(7 in numeros_aleatorios)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
original = [1, 2, 3]
# Crea una copia de la lista original llamada copia_1 usando slicing.
copia_1 = original[:]
# Crea otra copia llamada copia_2 usando copy().
copia_2 = original.copy()
# Crea una referencia a la lista original llamada referencia.
referencia = original
# Modifica el primer elemento de la lista referencia a 10.
referencia[0] = 10
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("Primera lista ", original)
print("Copia 1 ", copia_1)
print("Copia 2 ", copia_2)
print("Referencia ", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)