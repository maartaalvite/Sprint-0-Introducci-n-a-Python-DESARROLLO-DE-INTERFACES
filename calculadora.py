from operaciones import suma, resta, multiplicacion, division

def calculadora():
    continuar = "s"

    while continuar == "s":
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Introduce números válidos")
            continue

        print("\n¿Qué operación deseas realizar?")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")

        operacion = input("Selecciona una opción (1-4): ")

        if operacion == "1":
            print("Resultado:", suma(num1, num2))
        elif operacion == "2":
            print("Resultado:", resta(num1, num2))
        elif operacion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif operacion == "4":
            print("Resultado:", division(num1, num2))
        else:
            print("Opción inválida.")

        continuar = input("\n¿Deseas realizar otra operación? (s/n): ")

    print("¡Hasta luego!")


#El if main sirve para ejecutar el codigo que haya dentro de el
if __name__ == "__main__":
    calculadora()
