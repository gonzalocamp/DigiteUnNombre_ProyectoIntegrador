import sys
import time
from conexion import DAO


# Aqui se guardan las funciones necesarias para la ejecucion del programa y el uso del
# metodo CRUD, como tambien el ingreso al sistema por medio de clave entre otras cosas.


def listarPacientes(pacientes):
    dao = DAO()  # Crear una instancia de la clase DAO
    registro = dao.listarPacientes()  # Obtener el registro de pacientes utilizando el método listarPacientes() de la
    # instancia dao
    # mostrar resultados en consola
    time.sleep(1)
    print("los datos a continuacion estan por Nombre, altura y peso")
    print("los pacientes cargados son : ")
    contador = 1  # Inicializar un contador para numerar los pacientes
    for fila in registro:
        time.sleep(1)
        # Crear una cadena de texto formateada con los datos del paciente
        datos = f"\nID: {fila[0]} Nombre: {fila[1]} | Altura: {fila[2]} Cmts.| Peso {fila[3]} Kg.:"
        print(
            datos.format(contador, fila[0], fila[1], fila[2], fila[3]))  # Imprimir los datos del paciente en la consola
        contador += 1  # Incrementar el contador
    print(" ")  # Imprimir una línea vacía al final para mayor claridad


def pedirDatosRegistro():
    # Solicitar al usuario que ingrese el nombre, altura y peso del paciente
    nombre = input("Ingrese el nombre: ")
    altura = input("Ingrese la altura en Centimetros: ")
    peso = input("Ingrese el peso: ")
    # Crear una tupla con los datos ingresados por el usuario
    datos = (nombre, altura, peso)
    # Llamar a la función "score" para realizar un cálculo con el peso y la altura
    score(int(peso), int(altura))
    # Devolvemos la tupla de datos ingresados por el usuario
    return datos


def pedirDatosEliminacion(pacientes):
    listarPacientes(pacientes)  # Mostrar la lista de pacientes utilizando la función listarPacientes()
    codigoEliminar = int(input(
        "Ingrese el código del paciente a eliminar: "))  # Solicitar al usuario que ingrese el código del paciente a
    # eliminar
    return codigoEliminar  # Devolver el código del paciente a eliminar


def pedirDatosActualizacion(pacientes):
    listarPacientes(pacientes)  # Mostrar la lista de pacientes utilizando la función listarPacientes()
    # Solicitar al usuario que ingrese el código del paciente a editar
    codigoEditar = input("ingrese el codigo del paciente a editar: ")
    # ingresos de datos de los pacientes a actualizar
    nombre = input("Ingrese el nombre a modificar: ")
    altura = input("Ingrese la altura a modificar: ")
    peso = input("Ingrese el peso a modificar: ")
    # Crear una tupla con los datos ingresados por el usuario y el código del paciente a editar
    datos = (nombre, altura, peso, codigoEditar)
    return datos  # Devolver la tupla de datos para su uso posterior


def ingresoClave():
    intentos = 0  # Inicializar el contador de intentos en 0
    passcode = 0  # Inicializar la variable passcode en 0
    i = 0  # no usamos esta variable
    while passcode != 12345 and intentos < 4:
        # Solicitar al usuario que ingrese la contraseña como un número entero
        passcode = int(input("\nPor favor, ingrese su contraseña: "))
        print(" ")

        if passcode == 12345:  # se ingresa al sistema
            print("Contraseña correcta! Bienvenido.")
        else:
            print("Contraseña incorrecta!")
            intentos += 1  # Incrementar el contador de intentos
            print("Intentos realizados:", intentos)
            if intentos == 4:  # si el contador de intentos llega 4 el sistema se bloquea
                print(" ")
                print("///////////////////////////////////////////////////////")
                print("Usuario bloqueado. Contacte al administrador del sistema")
                print("///////////////////////////////////////////////////////")
                print(" ")
                print("Cerrando programa")
                print(" ")
                print("by Digite un nombre soft(Patente pendiente)")
                time.sleep(1)
                print(" ")
                sys.exit()


# Explicacion del funcionamiento del ingreso clave:
# Se inicializa el contador de intentos en 0 y la variable passcode en 0. Luego, se ejecuta un bucle while que
# continuará hasta que la contraseña ingresada sea igual a 12345 o se haya superado el límite de intentos (4 intentos
# en este caso). Si la contraseña ingresada es igual a 12345, se muestra un mensaje de "Contraseña correcta!
# Bienvenido.". Si la contraseña es incorrecta, se muestra un mensaje de "Contraseña incorrecta!" y se incrementa el
# contador de intentos. Luego se muestra la cantidad de intentos realizados. Si se alcanza el límite de 4 intentos,
# se muestra un mensaje de "Usuario bloqueado. Contacte al administrador del sistema" y se finaliza el programa.


def score(peso, altura):
    # Cálculo del IMC
    calculo = (peso / altura ** 2) * 100
    print("Calculando el IMC, espera por favor")
    time.sleep(3)  # Esperar 3 segundos
    print(" ")
    # Mostrar el resultado del IMC
    print(f"El IMC del paciente ingresado es: {calculo}")
    print("Comparando resultaddo con tabla IMC")
    print(" ")
    time.sleep(2)
    # Mostrar mensaje de comparación con la tabla IMC
    # Comparar el resultado del IMC con los rangos establecidos y mostrar el mensaje correspondiente
    if calculo < 0.19 or calculo >= 0.25:
        print("El paciente ingresado necesita intervención nutricional. Contactar con el nutricionista.")
        print(" ")
    else:
        print("El paciente ingresado no necesita intervención nutricional.")
        print(" ")
    return calculo  # Devolver el valor del IMC calculado
# En este código, la función score() se encarga de calcular el Índice de Masa Corporal (IMC) y mostrar el resultado,
# así como realizar una comparación con los rangos establecidos para determinar si el paciente necesita intervención
# nutricional.
