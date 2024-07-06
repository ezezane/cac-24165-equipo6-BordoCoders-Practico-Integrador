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
        sql = """SELECT * FROM productos ORDER BY id DESC"""
        # consulta
        cursor.execute(sql)
        productos = cursor.fetchall()
        # return resultados
        return productos


def ReadOneProduct(id):
    conexion = conectarMySQL()
    prod = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM productos WHERE id = %s", (id,))
        prod = cursor.fetchone()
    conexion.close()
    return prod


# función para crear nuevos registros en la base de datos
# TODO: actualizar los valores por las variables
def CreateDB(marca,nombre,precio,imagen):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO productos (marca, nombre, precio, imagen) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql,(marca,nombre,precio,imagen))
        conexion.commit()
        conexion.close()


# función para actualizar un producto de la base en función del ID
# TODO: actualizar los valores por las variables
def UpdateDB(marca,nombre,precio,url,id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET marca = %s, nombre = %s, precio = %s, imagen = %s WHERE id = %s",(marca,nombre,precio,url,id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result







# función para eliminar un producto de la base en función del ID
# TODO: actualizar los valores por las variables
def DeleteDB():
    # conexion mysql
    conexion = conectarMySQL()
    sql = "DELETE FROM productos WHERE id = '';"
