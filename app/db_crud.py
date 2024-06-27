import pymysql
from db_conection import *

# función para hacer la llamada a la base y traer todos los productos
# esto devuelve una tupla, la cual hay que recorrerla para mostrarla
def ReadProductos():
    # conexion mysql
    conexion = conectarMySQL()
    productos = []
    with conexion.cursor() as cursor:
        # Consulta a la base
        sql = """SELECT * FROM productos"""
        # consulta
        cursor.execute(sql)
        productos = cursor.fetchall()
        # return resultados
        return productos


# función para crear nuevos registros en la base de datos
# TODO: actualizar los valores por las variables
def CreateDB():
    # conexion mysql
    conexion = conectarMySQL()

    with conexion.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO 'productos' ('marca', 'nombre', 'precio', 'imagen') VALUES ()"
        cursor.execute(sql)
        conexion.commit()


# función para actualizar un producto de la base en función del ID
# TODO: actualizar los valores por las variables
def UpdateDB():
    # conexion mysql
    conexion = conectarMySQL()
    sql = "UPDATE 'productos' SET marca = '', nombre = '', precio = '', imagen = '' WHERE id = '';"


# función para eliminar un producto de la base en función del ID
# TODO: actualizar los valores por las variables
def DeleteDB():
    # conexion mysql
    conexion = conectarMySQL()
    sql = "DELETE FROM productos WHERE id = '';"
