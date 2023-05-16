from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Proveedores import Proveedores, ProveedoresSchema

routes_Proveedores = Blueprint("routes_Proveedores", __name__)

#PRODUCTO - Schema 
Proveedore_Schema = ProveedoresSchema()
Proveedores_Schema = ProveedoresSchema(many=True)

@routes_Proveedores.route('/Proveedores', methods=['GET'] )
def Proveedores():
    return "Proveedores  || ¡Hello people!"

#||||||||||||||||SAVE/CREAR|||||||||||||||||||||

@routes_Proveedores.route('/Guardar_Proveedor', methods=['POST'] )
def Guardar_Proveedor():
    
    Prove = request.json ['N_Prov']
    print(Prove)
    new_Prove = Prove(Prove)
    db.session.add(new_Prove)
    db.session.commit()
    return redirect('/viewProvedor')

#||||||||||||||||VIEW|||||||||||||||||||||

@routes_Proveedores.route('/viewProvedor', methods=['GET'])
def view_Provedor():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = Proveedores.query.all()    
        result_Provedor = Proveedores_Schema.dump(returnall)
        return jsonify(result_Provedor)
    else:
        return vf
    
    #||||||||||||||||ELIMINAR|||||||||||||||||||||
    
@routes_Proveedores.route('/clearCat', methods=['GET'] ) 
def eliminar_Provedor(id):
    prove = Proveedores.query.get(id)
    db.session.delete(prove)
    db.session.commit()
    return jsonify(Proveedores_Schema.dump(prove)) 

#||||||||||||||||ACTUALIZAR|||||||||||||||||||||

@routes_Proveedores.route('/updateProd', methods=['POST'] )
def actualizar_Prod():
    id = request.json['id']
    new_prove = request.json['N_Prove']
    Descripcion = request.json['Descripcion']
    updateProd = Proveedores.query.get(id)
    updateProd.nameProve= new_prove
    updateProd.descripProve = Descripcion
    db.session.commit()
    return redirect('/Provedores')