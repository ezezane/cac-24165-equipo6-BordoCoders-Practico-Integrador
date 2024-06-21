from flask import Flask, render_template

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


# LISTADO DE PRODUCTOS
@app.route("/productos")
def cargar_productos():
    title = 'Productos | Perfumería Borbocoders'
    return render_template("productos.html",title=title)


# --------------------
# PÁGINAS DEL BACK-END
# --------------------


# HOME / LISTADO DE PRODUCTOS CARGADOS


# CREAR NUEVO PRODUCTO


# EDITAR PRODUCTO


# ELIMINAR PRODUCTO
