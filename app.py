from flask import Flask, render_template, request
import pymysql

app = Flask(_name_)

# Conexion a la base de datos
def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="redes_sociales_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Guardar datos del formulario
@app.route("/guardar", methods=["POST"])
def guardar():

    nom = request.form["nombre"]
    cor = request.form["correo"]
    ed = request.form["edad"]
    red = request.form["red_social"]
    uso = request.form["uso"]
    apr = request.form["aprendizaje"]
    hor = request.form["horas"]

    try:
        con = obtener_conexion()
        cur = con.cursor()

        sql = """INSERT INTO registros
        (nombre, correo, edad, red_social, uso,
        aprendizaje, horas)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        cur.execute(sql, (nom, cor, ed, red, uso, apr, hor))

        con.commit()

        cur.close()
        con.close()

        return render_template(
            "index.html",
            mensaje="¡Encuesta registrada correctamente!"
        )

    except Exception as e:
        return render_template(
            "index.html",
            mensaje="Error al guardar los datos: " + str(e)
        )


if _name_ == "_main_":
    app.run(debug=True)