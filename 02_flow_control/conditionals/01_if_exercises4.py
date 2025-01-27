import os 

os.system("clear")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Ingrese su edad para calificarla: "))

if age < 2: 
    print("Es un bebé")
elif age >= 3 and age <= 12: 
    print("Es un niño")
elif age >= 13 and age <=17:
    print("Es un Adolescente")
elif age >= 13 and age <=17:
    print("Es un Adolescente")
elif age >= 18 and age <=64: # 3 <= edad <= 12
    print("Es un Adulto")
elif age >= 65:
    print("Adulto mayor")