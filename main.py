from flask import Flask, render_template, request
from flask import g
from flask_wtf.csrf import CSRFProtect 
from flask import flash
import forms

app = Flask(__name__)
app.secret_key="Esta es la clave secreta"
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre="Mario"
    print(' Before request 1')

@app.after_request
def after_request(response):
    print('After request 3')
    return response

@app.route('/')
def index():
    lista = {"betillo", "betillo", "antoi"}
    print("Index 2")
    print("Hola {}".format(g.nombre))
    grupo = "IDGS-803"
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    matricula=""
    nombre=""
    edad=""
    correo=""
    ape=""
    #obtendra los valores de formulario por default
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():
        matricula=alumno_clase.matricula.data
        nombre=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.correo.data
        mensaje='Bienvenido {}'.format(nombre)
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clase,matricula=matricula,nombre=nombre,ape=ape,edad=edad,correo=correo)

PRECIO_BOLETA = 12.00

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    total_a_pagar = None
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cantidad_boletas = int(request.form.get('cantidad_boletos'))
        usar_cineco = request.form.get('cineco') == 'si'
        cantidadCompradores = request.form.get('cantidad_compradores')

        if cantidad_boletas < 1 or cantidad_boletas > 7:
            error = "La cantidad de boletas debe estar entre 1 y 7."
            return render_template('cinepolis.html', total_a_pagar=total_a_pagar, error=error)
        if cantidad_boletas > (cantidadCompradores*7):
            error="cantidad erronea"
            return render_template('cinepolis.html', total_a_pagar=total_a_pagar, error=error)
        else:
            total = cantidad_boletas * PRECIO_BOLETA

            if cantidad_boletas > 5:
                total *= 0.85 
            elif 3 <= cantidad_boletas <= 5:
                total *= 0.90 

            if usar_cineco:
                total *= 0.90

            total_a_pagar = round(total, 2)

    return render_template('cinepolis.html', total_a_pagar=total_a_pagar, error=error)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplomacro1')
def ejemplomacro1():
    return render_template("ejemplomacro1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/OperaBas")
def Operas():
    return render_template("OperaBas.html")

@app.route("/Resultado", methods=["GET","POST"])
def Resultado():
    if request.method == "POST":
        num1 = request.form.get("N1")
        num2 = request.form.get("N2")
        resultado = int(num2) + int(num1)
        return render_template("OperaBas.html", resultado=resultado)

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}"

@app.route("/edad/<int:edad>")
def felicitacion(edad):
    return f"Feliz cumple {edad}"

@app.route("/edad/<int:edad>/nombre/<string:nombre>")
def felicitaciones(edad, nombre):
    return f"Feliz cumple número {edad}, amigo {nombre}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {}".format(n1 + n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="pepe"):
    return "El nombre de Nom es " + nom

@app.route("/form1")
def form1():
    return '''
    <form action="/cinepolis" method="POST">
        <label>Nombre:</label>
        <input type="text" name="nombre1" placeholder="Nombre" required><br>

        <label>Cantidad de compradores:</label>
        <input type="number" name="Cantidad1" placeholder="Cantidad" required><br>

        <label>Cantidad de boletos:</label>
        <input type="number" name="CantidadBoletos1" placeholder="Cantidad de boletos" required><br>

        <label>Tarjeta Cineco:</label>
        <input type="radio" name="cineco1" value="Si" required> Sí
        <input type="radio" name="cineco1" value="No" required> No <br>

        <button type="submit">Calcular</button>
    </form>
    '''

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
