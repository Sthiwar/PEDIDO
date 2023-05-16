from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma


#model
from Model.Clientes import Clientes
from Model.Productos import Productos
from Model.Proveedores import Proveedores
from Model.RegistroPedido import RegistroPedido
from Model.Repartidor import Repartidor


#import bluplin



@app.route("/")
def index():
    titulo="Pagina Principal"
    return render_template('/main/index.html', titulo=titulo)    

# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')