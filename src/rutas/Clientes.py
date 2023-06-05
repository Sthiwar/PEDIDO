from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Clientes import Clientes, ClientesSchema
from Model.Repartidor import Repartidor

routes_Cliente = Blueprint("routes_Cliente", __name__)

#CLIENTE - Schema 
Cliente_schema = ClientesSchema()
Clientes_Schema = ClientesSchema(many=True)




@routes_Cliente.route('/Guardar_Clientes', methods=['POST'])
def Guardar_Clientes():
    tipoPersona = request.form['tipoPersona']
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    password = request.form['password']
    usuario = request.form['usuario']
    telefono = request.form['telefono']
    direccion = request.form['direccion'] if tipoPersona == 'PersonaNormal' else ''  # Obtener 'direccion' solo si es 'PersonaNormal', de lo contrario, asignar un valor predeterminado vacío
    
    if tipoPersona == 'PersonaNormal':
        new_cli = Clientes(NombreC, Email, password, usuario, telefono, direccion)
        db.session.add(new_cli)
        db.session.commit()
    elif tipoPersona == 'Repartidor':
        new_rep = Repartidor(NombreC, Email, password, usuario, telefono)
        db.session.add(new_rep)
        db.session.commit()
        
    return "si"

@routes_Cliente.route("/validar_login", methods=["POST"])
def validar_login():
    
    Email = request.json["Email"]
    password = request.json["password"]

    verificacion_cliente = Clientes.query.filter_by(Email=Email, password=password).first()
    verificacion_repartidor = Repartidor.query.filter_by(Email=Email, password=password).first()

    # Busca el usuario en la base de datos
    if verificacion_cliente or verificacion_repartidor:
        return "Correcto"
    else:
        return "Incorrecto"