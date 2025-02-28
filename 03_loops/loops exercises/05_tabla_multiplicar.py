# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

number = int(input("Introduce un número: "))
i = 1

print(f"Tabla de multiplicar del {number}:")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i +=1

