# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

number = int(input("Enter a number: "))
multiplicador = 1

while  multiplicador <= 10:
    print(f' {number} x {multiplicador} = {number * multiplicador}')
    multiplicador += 1


