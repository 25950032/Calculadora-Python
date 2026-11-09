
# =====================================
# CALCULADORA BASICA EN PYTHON
# Autor: Raquel Klepache
# =====================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


# Programa principal

while True:

    print("\n===== CALCULADORA PYTHON =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("\nSelecciona una operación: ")

    if opcion == "5":
        print("¡Gracias por utilizar la calculadora!")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción incorrecta. Intenta nuevamente.")
        continue

    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        match opcion:
            case "1":
                resultado = sumar(numero1, numero2)

            case "2":
                resultado = restar(numero1, numero2)

            case "3":
                resultado = multiplicar(numero1, numero2)

            case "4":
                resultado = dividir(numero1, numero2)

        print(f"\nResultado: {resultado}")

    except ValueError:
        print("Error: Debes ingresar números válidos.")
