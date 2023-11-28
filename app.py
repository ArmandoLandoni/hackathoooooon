from flask import Flask, render_template, request, redirect, url_for, render_template_string, flash
import folium
from folium.plugins import MarkerCluster
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from database import create_db
from models import Task,User
from forms import LoginForm, RegisterForm, TaskForm





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
    tasks = Task.query.filter_by(user_id=current_user.id)
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data,user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
      
    return render_template("index.html",tasks=tasks,form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'danger')

    return render_template('login.html', form=form)





@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))






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
    m = folium.Map(location=(-23.442503, -58.443832), zoom_start=6, width=700, height=400)
    
    return m.get_root().render() 




@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        piel_caliente = request.form.get('piel_caliente').lower()
        dolor_de_cabeza = request.form.get('dolor_de_cabeza').lower()
        dolor_de_estomago = request.form.get('dolor_de_estomago').lower()
        comportamiento = request.form.get('comportamiento').lower()
        calambres = request.form.get('calambres').lower()
        sed = request.form.get('sed').lower()
        movimientos = request.form.get('movimientos').lower()

        puntos = 0

        if piel_caliente == 'si':
            puntos += 1

        if dolor_de_cabeza == "si":
            puntos += 1

        if dolor_de_estomago == "si":
            puntos += 1

        if comportamiento == "si":
            puntos += 2

        if calambres == "si":
            puntos += 1

        if sed == "si":
            puntos += 1

        if movimientos == "si":
            puntos += 1

        # Procesar los puntos y devolver la respuesta adecuada (puedes imprimir o renderizar un template).
        if puntos <= 3:
            resultado = "Al parecer no estás sufriendo de deshidratación, de todas formas, cuídate :)"
        elif puntos <= 6:
            resultado = "Estás moderadamente deshidratado, realiza los siguientes pasos: \n Evita bebidas con cafeína o con azúcar en exceso. \n Evita bebidas muy frías o muy calientes. \n Evita comidas pesadas. "
        else:
            resultado = "Estás altamente deshidratado. Sigue los siguientes consejos: \n Busca la sombra y evita la exposición al sol y al calor. \n Hidrátate a menudo, pero no mucha cantidad a la vez. \n Utiliza humectantes para suavizar tu piel seca \n Ve a un médico rápidamente para recibir un tratamiento adecuado."
        
        return resultado

    return render_template('test1.html')  # Nombre del template HTML que contiene el formulario
   

















































































@app.route('/estadistica')
def estadistica():

    return render_template_string('Hola mundo')




if __name__ == '__main__':
    app.run(debug=True)