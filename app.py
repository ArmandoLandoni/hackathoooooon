from flask import Flask, render_template, request, redirect, url_for, render_template_string, flash
import folium
from folium.plugins import MarkerCluster, HeatMap
import numpy as np
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from database import create_db
from models import Task,User
from forms import LoginForm, RegisterForm, TaskForm
import pandas as pd
from dash import Dash
from dash import dcc
from dash import html 
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go



#Instaciamos un objeto a partir de la clase flask
app = Flask(__name__)




# Configuraciones 
app = Flask(__name__)
app.config.from_object("config.Config")
db = create_db(app)




# Configuracion del login 
login_manager = LoginManager(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    # Esta función carga el usuario a partir de su ID almacenado en la sesión
    return User.query.get(int(user_id))


# Rutas 
@app.route("/", methods=['GET','POST'])
@login_required
def index():

    return redirect(url_for('inicio'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            return render_template("error.html")
        else:
            newUser = User(username=form.username.data,password=form.password.data)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for("login"))
        

    return render_template("register.html",form=form)




@app.route('/inicio')
def inicio():
    m = folium.Map(location=(-23.442503, -58.443832), zoom_start=6.5,min_zoom=6.5, max_zoom=12, width=1494, height=896)

    data = np.array([np.random.normal(-23.442503, 0.05, size=100),
                     np.random.normal(-58.443832, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-22.39746, 0.08, size=100),
                     np.random.normal(-61.25582, 0.05, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-22.39587, 0.09, size=100),
                     np.random.normal(-61.24559, 0.06, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-19.9208, 0.05, size=100),
                     np.random.normal(-61.7587, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-19.91314, 0.09, size=100),
                     np.random.normal(-61.7705, 0.06, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-19.91158, 0.08, size=100),
                     np.random.normal(-61.76035, 0.05, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
    
    data = np.array([np.random.normal(-22.47086, 0.07, size=100),
                     np.random.normal(-62.12252, 0.04, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.82469, 0.04, size=100),
                     np.random.normal(-59.99069, 0.01, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.81326, 0.09, size=100),
                     np.random.normal(-59.98668, 0.06, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.54259, 0.06, size=100),
                     np.random.normal(-59.30218, 0.03, size=100)]).T
    HeatMap(data, radius=18).add_to(m)
#ASUNCION
    data = np.array([np.random.normal(-25.2862937, 0.08, size=100),
                     np.random.normal(-57.5618486, 0.05, size=100)]).T
    HeatMap(data, radius=19).add_to(m)

    data = np.array([np.random.normal(-19.54255, 0.09, size=100),
                     np.random.normal(-59.30706, 0.04, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.53386, 0.07, size=100),
                     np.random.normal(-59.26474, 0.04, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.52774, 0.09, size=100),
                     np.random.normal(-60.11245, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-19.52263, 0.06, size=100),
                     np.random.normal(-60.11885, 0.01, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.67604, 0.07, size=100),
                     np.random.normal(-59.9646, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.67591, 0.09, size=100),
                     np.random.normal(-59.97931, 0.07, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.67192, 0.05, size=100),
                     np.random.normal(-60.00072, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.6719, 0.06, size=100),
                     np.random.normal(-59.98589, 0.03, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.66299, 0.05, size=100),
                     np.random.normal(-59.9765, 0.02, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.65897, 0.08, size=100),
                     np.random.normal(-59.9979, 0.03, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.65897, 0.09, size=100),
                     np.random.normal(-59.98311, 0.05, size=100)]).T
    HeatMap(data, radius=18).add_to(m)

    data = np.array([np.random.normal(-20.40015, 0.04, size=100),
                     np.random.normal(-60.57153, 0.01, size=100)]).T
    HeatMap(data, radius=18).add_to(m)



    m = m.get_root()._repr_html_()

    
    return render_template("inicio.html", m=m)



@app.route('/test1')
def test1():
    
    return render_template('test1.html')  



@app.route('/respuesta')
def respuesta():

    return render_template('respuesta.html')



@app.route('/test2')
def test2():
    
    return render_template('test2.html')  



@app.route('/respuesta2')
def respuesta2():

    return render_template('respuesta2.html')





@app.route('/faqs')
def faqs():

    return render_template('faqs.html')

































@app.route('/estadistica')
def estadistica():

    return render_template_string('Hola mundo')




if __name__ == '__main__':
    app.run(debug=True)