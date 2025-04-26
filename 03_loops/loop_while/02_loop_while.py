# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 0
suma = 0

while contador <= 20:
    if contador % 2 == 0:
        print(contador)
    contador += 1
    suma += contador

print('La suma de los numeros impares: ', suma)