# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

password = input("Introduzca una contraseña: ")

while len(password) < 8:
    password = input("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo: ")

print("Contraseña válida")