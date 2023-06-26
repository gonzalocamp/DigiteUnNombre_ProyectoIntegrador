import time
import psycopg2
from psycopg2 import errors


# en este archivo se guardan todos los codigos para acceder a la base de datos en el programa postgresql. creando una
# clase llamada DAO. Que significa DAO?? DAO significa "Data Access Object" (Objeto de Acceso a Datos, en español).
# Es un patrón de diseño de software que se utiliza en la capa de acceso a datos de una aplicación
# para abstraer y encapsular la lógica de acceso a la base de datos u otro medio de almacenamiento. El objetivo del
# patrón DAO es proporcionar una interfaz simple y coherente para interactuar con los datos, independientemente de la
# tecnología subyacente utilizada para el almacenamiento. Esto permite separar la lógica de negocio de los detalles
# de implementación del acceso a los datos.
#
# En el contexto del código proporcionado, DAO se refiere a una instancia de la clase DAO que se utiliza para
# realizar operaciones relacionadas con el acceso a la base de datos o almacenamiento de los pacientes. Las
# diferentes funciones, como listarPacientes(), registrarPaciente(), actualizarPaciente(), eliminarPaciente(),
# entre otras, se ejecutan en el objeto dao para interactuar con los datos y realizar las operaciones
# correspondientes en la capa de acceso a datos.

class DAO:
    def __init__(self):
        try:
            # Establecer la conexión con la base de datos PostgreSQ
            self.conexion = psycopg2.connect(
                user='postgres',
                password='34016174asd',
                host='127.0.0.1',
                port='5432',
                database='Nutricion'
            )
            # Capturar errores de conexión
        except errors:
            print("Error al intentar la conexion: ")

    def listarPacientes(self):

        if self.conexion:
            try:
                # Crear un cursor para ejecutar consultas SQL
                cursor = self.conexion.cursor()
                # Ejecutar la consulta SQL para obtener todos los registros
                cursor.execute("SELECT * FROM pacientes")
                # Obtener todos los resultados de la consulta
                resultado = cursor.fetchall()
                # Retornar resultados
                return resultado
            except errors:
                print("error al intentar la conexion")

    # Dentro del método, se realiza lo siguiente:
    #
    # Se verifica si la conexión a la base de datos (self.conexion) existe. Si la conexión existe, se crea un cursor
    # utilizando self.conexion.cursor(). El cursor se utiliza para ejecutar consultas SQL en la base de datos. Se
    # ejecuta la consulta SQL "SELECT * FROM pacientes" para obtener todos los registros de la tabla "pacientes". Se
    # utiliza cursor.fetchall() para obtener todos los resultados de la consulta y se almacenan en la variable
    # resultado. Se retorna el resultado obtenido.

    def registrarPaciente(self, datos):
        try:
            # Establecer la conexión con la base de datos PostgreSQL
            self.conexion = psycopg2.connect(
                user='postgres',
                password='34016174asd',
                host='127.0.0.1',
                port='5432',
                database='Nutricion'
            )
            # Crear un cursor para ejecutar consultas SQL
            cursor = self.conexion.cursor()
            # Definir la consulta SQL para insertar un nuevo registro
            sql = "INSERT INTO pacientes (nombre, altura, peso) VALUES(%s, %s, %s)"
            # Ejecutar la consulta SQL con los datos proporcionados
            cursor.execute(sql, datos)
            # Confirmar los cambios en la base de datos
            self.conexion.commit()
        except errors.DatabaseError as e:
            # Capturar errores de conexión o inserción de datos
            print("Error al conectarse o insertar datos:", str(e))

    # Dentro del método, se realiza lo siguiente:
    #
    # Se establece la conexión con la base de datos utilizando los detalles de autenticación proporcionados. Se crea
    # un cursor utilizando self.conexion.cursor() para ejecutar consultas SQL. Se define la consulta SQL para
    # insertar un nuevo registro en la tabla "pacientes". La consulta utiliza marcadores de posición %s para los
    # valores de nombre, altura y peso. Se ejecuta la consulta SQL utilizando cursor.execute(sql, datos), donde datos
    # es una tupla que contiene los valores de nombre, altura y peso proporcionados. Se utiliza self.conexion.commit(
    # ) para confirmar los cambios en la base de datos y guardar el nuevo registro. Si se produce algún error durante
    # la conexión a la base de datos o la inserción de datos, se captura la excepción errors.DatabaseError y se
    # muestra un mensaje de error en la consola. En resumen, este método permite insertar un nuevo registro de
    # paciente en la tabla "pacientes" de la base de datos.

    def eliminarPaciente(self, codigoEliminar):
        try:
            self.conexion = psycopg2.connect(
                # Establecer la conexión con la base de datos PostgreSQL
                user='postgres',
                password='34016174asd',
                host='127.0.0.1',
                port='5432',
                database='Nutricion'
            )
            # Crear un cursor para ejecutar consultas SQL
            cursor = self.conexion.cursor()
            # Definir la consulta SQL para eliminar un registro
            sql = "DELETE FROM pacientes WHERE idpaciente=%s"
            # Ejecutar la consulta SQL con el código de paciente
            cursor.execute(sql, (codigoEliminar,))
            # Confirmar los cambios en la base de datos
            self.conexion.commit()
            # Mostrar mensaje de éxito
            print("Paciente Eliminado correctamente")
            print(" ")
            time.sleep(2)

        except Exception as e:
            # Capturar errores de conexión u otros errores
            print("Error al conectar:", str(e))

        # Dentro del método, se realiza lo siguiente:
        #
        # Se establece la conexión con la base de datos utilizando los detalles de autenticación proporcionados. Se
        # crea un cursor utilizando self.conexion.cursor() para ejecutar consultas SQL. Se define la consulta SQL
        # para eliminar un registro de la tabla "pacientes" utilizando el código de paciente como condición. Se
        # ejecuta la consulta SQL utilizando cursor.execute(sql, (codigoEliminar,)), donde codigoEliminar es el
        # código del paciente que se desea eliminar. Se utiliza self.conexion.commit() para confirmar los cambios en
        # la base de datos y realizar la eliminación del registro. Se muestra un mensaje de éxito indicando que el
        # paciente ha sido eliminado correctamente. Se realiza una pausa de 2 segundos antes de continuar. Si se
        # produce algún error durante la conexión a la base de datos u otros errores, se captura la excepción
        # Exception y se muestra un mensaje de error en la consola. En resumen, este método permite eliminar un
        # registro de paciente de la tabla "pacientes" en la base de datos.

    def actualizarCurso(self, pedirDatosActualizacion):
        try:
            # Establecer la conexión con la base de datos PostgreSQL
            self.conexion = psycopg2.connect(
                user='postgres',
                password='34016174asd',
                host='127.0.0.1',
                port='5432',
                database='Nutricion'
            )
            # Crear un cursor para ejecutar consultas SQL
            cursor = self.conexion.cursor()
            # Definir la consulta SQL para actualizar un registro de la tabla
            sql = "UPDATE pacientes SET nombre=%s, altura=%s, peso=%s WHERE idpaciente=%s"
            # Ejecutar la consulta SQL con los nuevos datos de actualización
            cursor.execute(sql, pedirDatosActualizacion)
            # Confirmar los cambios en la base de datos
            self.conexion.commit()
            # Mostrar mensaje de éxito
            print("Paciente Actualizado correctamente")
            print(" ")
            time.sleep(2)
        except Exception as e:
            # Capturar errores de conexión u otros errores
            print("Error de conexion", str(e))
