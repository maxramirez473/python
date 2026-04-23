from negocio import (buscar_alumno, listar_alumnos, cantidad_alumnos, agregar_nuevo_alumno, eliminar_alumno_por_legajo, modificar_alumno_por_legajo)
import time 
import os

def clear_screen():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear') 

def menu():
    clear_screen()
    print("1. Listar alumnos")
    print("2. Buscar alumno por legajo")
    print("3. Cantidad de alumnos")
    print("4. Agregar nuevo alumno")
    print("5. Eliminar alumno por legajo")
    print("6. Modificar alumno por legajo")
    print("7. Salir")


def pedir_legajo(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        print("El legajo no puede estar vacio.")
        time.sleep(2)
        return None

    try:
        return int(valor)
    except ValueError:
        print("Legajo invalido. Debe ser un numero entero.")
        time.sleep(2)
        return None


def ejecutar_programa():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                alumnos = listar_alumnos()
                print(alumnos)
                time.sleep(10)
            case "2":
                legajo = pedir_legajo("Ingrese el legajo del alumno: ")
                if legajo is None:
                    continue

                alumno = buscar_alumno(legajo)
                if alumno.empty:
                    print("No se encontro un alumno con ese legajo.")
                else:
                    print(alumno)
                time.sleep(5)
            case "3":
                cantidad = cantidad_alumnos()
                print(f"Cantidad de alumnos: {cantidad}")
                time.sleep(5)
            case "4":
                legajo = pedir_legajo("Ingrese el legajo del nuevo alumno: ")
                nombres = input("Ingrese los nombres del nuevo alumno: ")
                email = input("Ingrese el email del nuevo alumno: ")
                if legajo is None or not nombres.strip() or not email.strip(): # Verifica que el legajo no sea None y que los nombres y email no estén vacíos después de eliminar espacios en blanco
                    print("Todos los campos son obligatorios. Por favor, intente nuevamente.")
                    time.sleep(2)
                    continue

                resultado = agregar_nuevo_alumno(legajo, nombres, email)
                print(resultado)
                time.sleep(5)
            case "5":
                legajo = pedir_legajo("Ingrese el legajo del alumno a eliminar: ")
                if legajo is None:
                    continue

                resultado = eliminar_alumno_por_legajo(legajo)
                print(resultado)
                time.sleep(5)
            case "6":
                legajo = pedir_legajo("Ingrese el legajo del alumno a modificar: ")
                if legajo is None:
                    continue

                nuevos_nombres = input("Ingrese los nuevos nombres del alumno (deje en blanco para no modificar): ")
                nuevo_email = input("Ingrese el nuevo email del alumno (deje en blanco para no modificar): ")

                if not nuevos_nombres.strip() and not nuevo_email.strip():
                    print("No se proporcionaron cambios. Por favor, intente nuevamente.")
                    time.sleep(2)
                    continue

                resultado = modificar_alumno_por_legajo(legajo, nuevos_nombres, nuevo_email)
                print(resultado)
                time.sleep(5)
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida. Por favor, seleccione una opcion del 1 al 7.")
                time.sleep(5)

if __name__ == "__main__":
    ejecutar_programa()