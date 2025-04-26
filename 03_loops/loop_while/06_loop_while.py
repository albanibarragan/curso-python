# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

# Paso 1: Pedir al usuario un número N
n = int(input('Ingrese un número positivo: '))

# Paso 2: Comenzamos desde el primer número primo
num = 2

# Paso 3: Vamos a revisar todos los números desde 2 hasta n
while num <= n:
    es_primo = True  
    divisor = 2    

    # Paso 4: Verificamos si tiene algún divisor entre 2 y num-1
    while divisor < num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1

    # Paso 5: Si no se encontró divisor, es primo
    if es_primo:
        print(num, end=" ")  # Imprimir en la misma línea

    # Paso 6: Pasamos al siguiente número
    num += 1
