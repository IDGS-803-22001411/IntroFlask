from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange,Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SearchField, DecimalField, EmailField
from wtforms import validators

class UserForm(Form):
    matricula = StringField("Matricula",[
        validators.DataRequired("este campo es requerido"),
        validators.Length(min=2,max=10,message="entre 3 y 10")
    ])
    edad = IntegerField("Edad",[
        validators.DataRequired("CaMPOobligatorio")
    ])
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    correo = EmailField("Correo",[
        validators.Email(message="correo no valido paps")
    ])