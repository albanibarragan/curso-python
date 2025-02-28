# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

number = int(input("introduzca un número entero positivo N "))  # Usuario ingresa un número
N = 2  # Aquí quieres comenzar desde el primer número primo


while N <= number:
    x = 2
    number_primo = True

    while x < N:
        if N % x == 0:
            number_primo = False
            break
        x += 1
    
    if number_primo:  
        print(N, "es primo")

    N += 1  # Pasamos al siguiente número 
print("Fin del programa. introduzca un número entero positivo N ")