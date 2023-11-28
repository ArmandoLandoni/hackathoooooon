'''
#RUTAS
@app.route('/')
def index():
    #Estirar datos de la base de datos
    participantes = Participante.query.all()
    mentor = {'nombre' : 'Edu','frase' : 'exactamente','edad' : 28}

    return render_template('index.html', participantes_html=participantes,mentor = mentor)


@app.route('/crear', methods=['POST'])
def crear():
    if request.method == 'POST' :
        #Obtener datos desde el from (desde un formulario)
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        edad = request.form.get('edad')
        estado_civil = request.form.get('estado_civil')
        
        #Creamos el objeto tipo participante
        participante = Participante(nombre=nombre, apellido=apellido, edad=edad, estado_civil=estado_civil)

        #Anadimos a la base de datos
        db.session.add(participante)
        db.session.commit()
        return redirect(url_for('index'))
    


@app.route('/eliminar/<id>')
def eliminar(id):
    #Obtener un solo participante a eliminar segun id
    participante = Participante.query.get(id)
    #Eliminar de la base de datos
    db.session.delete(participante)
    db.session.commit()
    #Mostrar en index
    return redirect(url_for('index'))




@app.route('/editar/<id>', methods = ['GET', 'POST'])
def editar(id):
    participante = Participante.query.get(id)
    if request.method == 'POST' :
        #Agarra la info del formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        edad = request.form.get('edad')
        estado_civil = request.form.get('estado_civil')
        #Cargar la info al objeto
        participante.nombre = nombre
        participante.apellido = apellido
        participante.edad = edad
        participante.estado_civil = estado_civil
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', participante=participante)

'''

































































