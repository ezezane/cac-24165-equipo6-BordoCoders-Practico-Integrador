from flask import Flask, render_template

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


# CREAR NUEVO PRODUCTO


# EDITAR PRODUCTO


# ELIMINAR PRODUCTO









# LISTADO DE PRODUCTOS JS
@app.route("/productos-js")
def cargar_productos_js():
    return render_template("productos.html",title=title)