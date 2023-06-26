# ::::::::::::Proyecto integrador de python::::::::::
#                     Requeriemientos
#             - Proyecto nuevo o anterior
#             - Incluir base de datos SQL o no SQL
#             - Video maximo de 30 minutos
#
# En el proyecto lo que decidimos fue utilizar el mismo programa que realizamos tanto en Pseint como en java,
# el cual es un programa destinado a los especialistas en nutrición, al mismo se le decidió agregarle algunas mejoras
# en el diseño y funcionamiento, como se lo relaciono con una base de datos de PostgreSql, programa que nos enseñaron
# a utilizar este semestre haciendo que el mismo funcione por medio del método CRUD, pero que significa el método
# este?, CRUD es el acrónimo de "Crear, Leer, Actualizar y Borrar" (del original en inglés: Créate, Read, Update and
# Delete) , que se usa para referirse a las funciones básicas en bases de datos que vamos a ir realizando mediante
# comandos en este programa, el cual va a ir enviando la información de los pacientes ingresados a la base de datos
# permitiéndome también actualizarlos, eliminarlos o solo consultar el listado de pacientes cargados, este cuenta con
# una funcionalidad el cual va a calcular el IMC y en base al cálculo le va a recomendar al profesional si el
# paciente tiene o no que recurrir a un plan nutricional.


import funciones  # Importamos desde funciones algunos metodos
from conexion import DAO  # Importamos la clase DAO
import time  # se importo la clase time para poner tiempos de espera en algas operaciones de la consola


def inicioSistema():  # le damos incio al sistema de nutricion
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("Bienvenido al Sistema de carga de pacientes y verificacion de peso")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    time.sleep(2)
    print(" ")
    print("Presione 1 para iniciar")
    print("Presione 2 para salir")
    print()
    time.sleep(1)
    opcion = int(input("Digite una opcion: "))  # Metodo input para ingresar la opcion
    print()

    # Utilizamos un IF para la variable opcion, dependiendo la elegida va a ingresar al
    # sistema o va a salir del mismo

    if opcion == 1:
        # Opción para listar pacientes
        print(f"Usted digito la opcion: {opcion}")
        print("ingresando....")
        time.sleep(1)
        funciones.ingresoClave()  # Solicitar clave de acceso
        menuPrincipal()  # Volver al menú principa
    elif opcion == 2:
        # Opción para salir del sistema
        print("Saliendo del sistema, hasta pronto.")
        print("By Digite un nombre soft(Patente pendiente)")
        return  # Finalizar la ejecución del programa
    else:  # Opción incorrecta
        print(" La opción seleccionada no es correcta ")
    print(":::::::::::::::::::::::::::")

    # Menu principal del metodo CRUD, ver explicacion al inicio del ejercicio


def menuPrincipal():
    continuar = True  # Mientras continuar sea verdadero se ejecuta el while
    while continuar:
        opcionCorrecta = False  # Opcion correcta va a ser falso
        while not opcionCorrecta:  # Mientras opcion correcta no sea falso, se ingresa al ciclo
            print("Ingresando al Sistema de carga de pacientes")
            print("Por Favor espere..!!")
            time.sleep(3)
            print(":::::::: Menu Principal ::::::::::")
            print(" ")
            print("1 - Listar")  # Read
            print("2 - registrar")  # Create
            print("3 - Actualizar")  # Update
            print("4 - Eliminar")  # Delete
            print("5 - Salir")
            print("::::::::::::::::::::::::::::::::::")
            opcion = int(input("Selecione una opcion: "))
            # Creamos un IF para controlar que la opcion seleccionada sea mayor que uno y menor que 5
            if opcion < 1 or opcion > 5:
                print("opcion incorrecta")
            elif opcion == 5:  # al seleccionar OP 5, la bandera continuar para ser falsa, por ende al volver al ciclo
                continuar = False  # el mismo no se ejecuta, finalizando con un break.
                print(" ")
                print("Cerrando programa espere por favor")
                time.sleep(1)
                print("....")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("..")
                time.sleep(0.5)
                print(".")
                time.sleep(1)
                print("Gracias por usar el sistema de carga y verificacion de peos")
                print(" ")
                print("by Digite un nombre soft(Patente pendiente)")

                print(" ")
                break
            else:  # En el caso que la opcion sea correcta ( sea un valor entre 1 y 5)
                opcionCorrecta = True
                ejecutarOpcion(opcion)  # se va a ejecutar la funcion ejecuarOpcion, dando inicio al uso del CRUD


# Funcion para ejecutar el metodo CRUD
def ejecutarOpcion(opcion):
    dao = DAO()  # Creamos una instancia para DAO
    if opcion == 1:  # Listar pacientes
        try:  # al elegir la opcion 1 el ssitema intentara lo siguiente
            pacientes = dao.listarPacientes()  # en la variable paciente el metodo ListarPacientes de la instancia DAO
            if len(pacientes) > 0:  # si la variables pacientes no esta vacia se ejeccuta la fauncion ListarPacientes
                funciones.listarPacientes(pacientes)
            else:
                print("No se encontró nada")  # en el caso de estar vacia , nos va a informar lo siguiente
        except Exception as e:  # nos va a mostrar el tipo de error que tiene, guardandolo en la variable e
            print("Ocurrió un error:", str(e))

    # Que es el metodo Exception? a sintaxis except Exception as e captura cualquier excepción que ocurra en el
    # bloque de código dentro del try y la asigna a la variable e. Luego, se imprime un mensaje de error que indica
    # que se produjo un error, seguido del mensaje de la excepción convertido a una cadena (str(e)). Es importante
    # destacar que capturar una excepción genérica como Exception puede ser útil para detectar y manejar cualquier
    # tipo de excepción , pero también puede ocultar problemas específicos o introducir un comportamiento de captura
    # demasiado amplio.

    elif opcion == 2:  # Registrar pacientes
        # Se solicitan los datos del paciente por la funcion pedirDatosRegistro
        pacientes = funciones.pedirDatosRegistro()
        try:
            dao = DAO()  # se crea una instancia de clase
            dao.registrarPaciente(
                pacientes)  # Se llama al método "registrarPaciente" de la instancia "dao" para registrar al paciente
            # con los datos proporcionados
            print(" ")
            print("Paciente registrado correctamente.")
            print(" ")
            print(" ")
        except Exception as e:
            print("Se produjo un error al registrar al paciente:", str(e))

    elif opcion == 3:  # Updatear pacientes
        try:
            pacientes = dao.listarPacientes()  # Se obtiene la lista de pacientes mediante el método
            # "listarPacientes()" de la instancia "dao"
            if len(pacientes) > 0:  # si la logitud de pacientes es mayor a 0, ingresamos al IF
                pacientes = funciones.pedirDatosActualizacion(pacientes)
                # # Se solicitan los datos de actualización del paciente mediante la función
                # "pedirDatosActualizacion()" de la variable "funciones"
                if pacientes:
                    dao.actualizarCurso(pacientes)
                    # Se solicitan los datos de actualización del paciente mediante la función
                    # "pedirDatosActualizacion()" de la variable "funciones"
                else:
                    print("ID paciente a actualizar no se encontro")
            else:
                print("No se econtro informacion")
        except Exception as e:
            print("No se econtraron pacientes", str(e))

    elif opcion == 4:  # Eliminar pacientes
        try:
            pacientes = dao.listarPacientes()  # Se obtiene la lista de pacientes mediante el método "listarPacientes(
            # )" de la instancia "dao"
            if len(pacientes) > 0:  # si la longitud es mayor a 0 entra al IF
                codigoEliminar = funciones.pedirDatosEliminacion(
                    pacientes)  # Se solicita el código del paciente a eliminar mediante la función
                # "pedirDatosEliminacion()" de la variable "funciones"
                if not (codigoEliminar == " "):
                    dao.eliminarPaciente(
                        codigoEliminar)  # Se llama al método "eliminarPaciente()" de la instancia "dao" para
                    # eliminar al paciente con el código proporcionado
                else:
                    print("El código ingresado no es válido.")
            else:
                print("No se encontraron pacientes para eliminar.")
        except ValueError:
            print("El código ingresado no es válido.")
        except Exception as e:
            print("Ocurrió un error:", str(e))

    else:  # Error al elegir la opcion
        print("Opción no válida....")


inicioSistema()  # Inicia el sistema
