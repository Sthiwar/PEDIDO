from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Repartidor import Repartidor, RepartidorSchema

routes_Repartidor = Blueprint("routes_Repartidor", __name__)

#Repartidor - Schema 
Repartidor_schema = RepartidorSchema()
Repartidor_Schema = RepartidorSchema(many=True)


@routes_Repartidor.route('/Guardar_Repartidor', methods=['POST'] )
def Guardar_Repartid():
    
    NombreC = request.form['NombreC']
    Email = request.form['Email']
    password = request.form['password']
    usuario = request.form['usuario']
    telefono = request.form['telefono']
    # problema = date.today()
    print(Nombre)
    new_rep = Repartidor( Nombre, Apellido,Email,password,usuario,telefono)
    db.session.add(new_rep)
    db.session.commit()
    return "si"