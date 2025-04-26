# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# Al menos un carácter especial (@, #, $, %, &, etc.).
print("\nEjercicio 4:")


while True:
    password = input('Introduce una contraseña: ')
    
    if len(password) < 8:
        print("❌ La contraseña debe tener al menos 8 caracteres.")
        continue

    if not password[0].isupper():
        print("❌ La primera letra debe ser una mayúscula.")
        continue

    if not any(c.islower() for c in password):
        print("❌ La contraseña debe tener al menos una letra minúscula.")
        continue

    print("✅ Contraseña válida.")
    break

