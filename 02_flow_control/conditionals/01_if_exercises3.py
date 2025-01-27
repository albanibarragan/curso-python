import os 

os.system("clear")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("---------Ejercicio 3 ------- ")
year = int(input("ingrese un año: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} es un año bisiestro")
else: 
    print(f"{year} no es un año bisiestro") 

