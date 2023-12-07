from flask import Flask, jsonify, render_template, request
from logueo import ejecucion


app = Flask(__name__, template_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\templateFiles', static_folder='C:\\Desarrollo\\Mis Proyectos\\WorkstationFedeOlivera\\main-Workstation\\FrontEnd\\HTML\\staticFiles' )


@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/forgot_password')
def forgot_password():
     return render_template('recuperarContraseña.html')

@app.route('/compras')
def compras():
     return render_template('compras.html')


@app.route('/login', methods=['POST'])
def login():

    data = request.get_json
    mail = data.__get__('mail')
    password = data.__get__('password')
    if not mail or not password:
        return jsonify({'mensaje': 'error en verificacion usuario/contraseña'})

    if ejecucion(mail, password):
        mensaje = 'ok'
    else:
        mensaje = 'error en verificacion usuario/contraseña'

    return jsonify({'mensaje': mensaje})



@app.route('/ventas')
def ventas():
     return render_template('ventas.html')

@app.route('/proveedores')
def proveedores():
     return render_template('proveedores.html')

@app.route('/productos')
def productos():
     return render_template('productos.html')

@app.route('/clientes')
def clientes():
     return render_template('clientes.html')



if __name__ == '__main__':
    app.run(debug=True)






