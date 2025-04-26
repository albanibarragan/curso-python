# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# 
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input('Introduzca una letra : ').lower()
contador = 0

for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")