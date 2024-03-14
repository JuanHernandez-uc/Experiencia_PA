from math import randint
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    print("Hola debes adivinar un numero del uno a al diez!")
    while True:
        input("Presiona enter para continuar")
        numero_usuario = int(input("Ingresa un numero del 0 al 10: "))
        numero_generado = int(randint(0,10))
        if numero_usuario == numero_generado:
            print("ES CORRECTO!!!")
        else:
            print("ta malo")
            print(f"El numero era {numero_generado}")
        continuar = int(input("Ingresa 1 para seguir jugando, 2 para salir: "))
        if continuar == 1:
            pass
        elif continuar == 2:
            break
