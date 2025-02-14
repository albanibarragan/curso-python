# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)


print("---------Ejercicio 2 ------- ")
print("------------CALCULARDORA--------- ")

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
operator = input("ingrese una operación (+, -, *, /): ")

if operator == "+":
    resultado = num1 + num2
elif operator == "-":
    resultado = num1 - num2
elif operator == "*":
    resultado = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
else:
    print("Operación no válida.")


print(resultado)