from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan","Pedro","Perez"]
    return render_template("index.html",grupo=grupo,lista=lista)

@app.route("/OperaBas")
def Operas():
    return render_template("OperaBas.html")

@app.route("/Resultado", methods=["GET","POST"])
def Resultado():
    if request.method=="POST":
        num1=request.form.get("N1")
        num2=request.form.get("N2")
        resultado=int(num2)+int(num1)
        return render_template("OperaBas.html",resultado=resultado)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "Hola!!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user,id):
    return f"Nombre: {user} ID: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="pedro"):
    return "El nombre de Nom es "+nom

@app.route("/foem1")
def form1():
    return '''
            <form>
            <label>Nombre:</lablel>
            <input type="text" name="nombre placeholder="Nombre"
            </br>
            <label>Nombre:</lablel>
            <input type="text" name="nombre placeholder="Nombre"
            </br>
            <label>Nombre:</lablel>
            <input type="text" name="nombre placeholder="Nombre"
            </br>
        </form>
        '''

if __name__ == '_main_':
    app.run(debug=True)