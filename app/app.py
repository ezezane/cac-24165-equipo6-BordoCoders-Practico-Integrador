from flask import Flask, render_template, request, redirect
from db_crud import *

app = Flask(__name__)

# ---------------------
# PÁGINAS DEL FRONT-END
# ---------------------

# HOME
@app.route("/")
def hello_world():
    title = 'Home | Perfumería Borbocoders'
    return render_template("frontend/index.html",title=title)


# SOBRE NOSOTROS
@app.route("/nosotros")
def cargar_nosotros():
    title = 'Sobre nosotros | Perfumería Borbocoders'
    return render_template("frontend/nosotros.html",title=title)


# CONTACTO
@app.route("/contacto")
def cargar_contacto():
    title = 'Quiero ser revendedor | Perfumería Borbocoders'
    return render_template("frontend/contact.html",title=title)


# LISTADO DE PRODUCTOS DB
@app.route("/productos")
def cargar_productos():
    title = 'Productos | Perfumería Borbocoders'
    productos = ReadProductos()
    return render_template("frontend/productos_db.html",title=title,productos=productos)


# --------------------
# PÁGINAS DEL BACK-END
# --------------------


# HOME / LISTADO DE PRODUCTOS CARGADOS
# LISTADO DE PRODUCTOS DB
@app.route("/admin")
def cargar_productos_admin():
    title = 'CRUD | Perfumería Borbocoders'
    productos = ReadProductos()
    return render_template("/backend/productos_db.html",title=title,productos=productos)



# CREAR NUEVO PRODUCTO
# paso 1 FORM
@app.route("/admin/crear")
def crear_productos_admin():
    title = 'Create | Perfumería Borbocoders'
    return render_template("/backend/form_create.html",title=title)

# paso 2 CREAR
@app.route("/cargar_producto", methods=['POST'])
def crear_productos_db():
    #print(request.form)
    prod_marca = request.form['marca']
    prod_name = request.form['name']
    prod_precio = request.form['precio']
    prod_URLimg = request.form['imgURL']
    result = CreateDB(prod_marca,prod_name,prod_precio,prod_URLimg)
    print(result)
    return redirect("/admin")



# EDITAR PRODUCTO
# paso 1 FORM precargado
@app.route("/admin/editar/<int:id>")
def editar_productos_form(id):
    productoID = ReadOneProduct(id)
    title = 'Update | Perfumería Borbocoders'
    return render_template("/backend/form_update.html",title=title,producto=productoID)

# paso 2 EDITAR
@app.route("/editar_producto", methods=['POST'])
def editar_productos_db():
    prod_id = request.form['prod_id']
    prod_marca = request.form['marca']
    prod_name = request.form['name']
    prod_precio = request.form['precio']
    prod_URLimg = request.form['imgURL']
    result = UpdateDB(prod_marca,prod_name,prod_precio,prod_URLimg,prod_id)
    print(result)
    return redirect("/admin")



# ELIMINAR PRODUCTO
# paso 1 FORM precargado
@app.route('/admin/borrar_producto/<int:id>')
def borrar_productos_form(id):
    productoID = ReadOneProduct(id)
    title = 'Delete | Perfumería Borbocoders'
    return render_template("/backend/form_delete.html",title=title,producto=productoID)

# paso 2 BORRAR
@app.route("/eliminar_producto/<int:id>", methods=['POST'])
def borrar_productos_db(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return redirect("/admin")