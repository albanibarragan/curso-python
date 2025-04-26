# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# 
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for num in numeros:
    while maximo < num:
        maximo = num
print(f"El número máximo es: {maximo}")