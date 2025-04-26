# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# 
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
'''
palabras_largas = []

for palabra in palabras:
    if len(palabra) > 4:
        palabras_largas.append(palabra)
print(palabras_largas)


'''

palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]

print(palabras_largas)