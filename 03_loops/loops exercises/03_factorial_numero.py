# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

number = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1

while contador <= number:
    factorial *= contador
    contador += 1

print(f"El factorial de {number} es: {factorial}")

