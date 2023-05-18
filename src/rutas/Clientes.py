from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Clientes import Clientes, ClientesSchema

routes_Cliente = Blueprint("routes_Cliente", __name__)

#CLIENTE - Schema 
Cliente_schema = ClientesSchema()
Clientes_Schema = ClientesSchema(many=True)


@routes_Cliente.route('/Guardar_Clientes', methods=['POST'] )
def Guardar_Client():
    
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Email = request.form['Email']
    password = request.form['password']
    usuario = request.form['usuario']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    # problema = date.today()
    print(Nombre)
    new_cli = cliente( Nombre, Apellido,Email,password,usuario,telefono, direccion,problema,id_paciente,id_odontologos)
    db.session.add(new_cli)
    db.session.commit()
    return "si"
    