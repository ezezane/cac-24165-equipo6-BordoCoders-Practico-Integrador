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
    return render_template("index.html",title=title)


# SOBRE NOSOTROS
@app.route("/nosotros")
def cargar_nosotros():
    title = 'Sobre nosotros | Perfumería Borbocoders'
    return render_template("nosotros.html",title=title)


# CONTACTO
@app.route("/contacto")
def cargar_contacto():
    title = 'Quiero ser revendedor | Perfumería Borbocoders'
    return render_template("contact.html",title=title)


# LISTADO DE PRODUCTOS DB
@app.route("/productos")
def cargar_productos():
    title = 'Productos | Perfumería Borbocoders'
    productos = ReadProductos()
    return render_template("productos_db.html",title=title,productos=productos)


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

# paso 2 CARGA
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


# ELIMINAR PRODUCTO









# LISTADO DE PRODUCTOS JS
@app.route("/productos-js")
def cargar_productos_js():
    return render_template("productos.html",title=title)