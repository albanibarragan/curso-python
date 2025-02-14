# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
import os
os.system("cls")


print("Ejercicio 2: listas")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print(numeros)