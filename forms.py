from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Correo electronico', validators=[DataRequired()])
    password = StringField('Numero de telefono', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegisterForm(FlaskForm):
    username = StringField('Correo electronico', validators=[DataRequired()])
    password = StringField('Numero de telefono', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class TaskForm(FlaskForm):
    title = StringField("Titulo", validators=[DataRequired()])
    description = StringField("Descripcion",validators=[DataRequired()])
    done = BooleanField("Completado")