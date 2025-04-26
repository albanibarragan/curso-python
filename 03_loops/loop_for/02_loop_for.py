# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:

# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
suma = 0

for num in numeros:
    suma += num

promedio = suma / len(numeros)
print(promedio)