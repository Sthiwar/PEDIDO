from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Clientes import Clientes, ClientesSchema

routes_Cliente = Blueprint("routes_cliente", __name__)

#CLIENTE - Schema 
Cliente_schema = ClientesSchema()
Clientes_Schema = ClientesSchema(many=True)

@routes_Cliente.route('/indexclientes', methods=['GET'] )
def indexClientes():
    return "Clientes || ¡Hello people!"

#||||||||||||||||SAVE/CREAR|||||||||||||||||||||

@routes_Cliente.route('/Guardar_Clientes', methods=['POST'] )
def Guardar_Clientes():
    
    client = request.json ['N_Cl']
    print(client)
    new_cli = Clientes(client)
    db.session.add(new_cli)
    db.session.commit()
    return redirect('/viewClientes')

#||||||||||||||||VIEW|||||||||||||||||||||

@routes_Cliente.route('/viewClientes', methods=['GET'])
def view_Clientes():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = Clientes.query.all()    
        result_Categoria = ClientesSchema.dump(returnall)
        return jsonify(result_Categoria)
    else:
        return vf
    
    #||||||||||||||||ELIMINAR|||||||||||||||||||||
    
@routes_Cliente.route('/clearCat', methods=['GET'] ) 
def eliminar_Clie(id):
    cli = Clientes.query.get(id)
    db.session.delete(cli)
    db.session.commit()
    return jsonify(ClientesSchema.dump(cli)) 

#||||||||||||||||ACTUALIZAR|||||||||||||||||||||

@routes_Cliente.route('/updateClientes', methods=['POST'] )
def actualizar_Cli():
    id = request.json['id']
    new_cli = request.json['N_cat']
    Descripcion = request.json['Descripcion']
    updateCli = Clientes.query.get(id)
    updateCli.nameClie = new_cli
    updateCli.descripCli = Descripcion
    db.session.commit()
    return redirect('/Clientes')