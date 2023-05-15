from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Productos import Productos, ProductosSchema

routes_Producto = Blueprint("routes_Producto", __name__)

#PRODUCTO - Schema 
Producto_Schema = Producto_chema()
Productos_Schema = Productos_Schema(many=True)

@routes_Producto.route('/Productos', methods=['GET'] )
def Productos():
    return "Productos || ¡Hello people!"

#||||||||||||||||SAVE/CREAR|||||||||||||||||||||

@routes_Producto.route('/Guardar_Producto', methods=['POST'] )
def Guardar_Producto():
    
    Product = request.json ['N_Product']
    print(Product)
    new_Product = Product(Product)
    db.session.add(new_Product)
    db.session.commit()
    return redirect('/viewProductos')

#||||||||||||||||VIEW|||||||||||||||||||||

@routes_Producto.route('/viewProductos', methods=['GET'])
def view_Productos():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = Productos.query.all()    
        result_Productos = Productos_Schema.dump(returnall)
        return jsonify(result_Productos)
    else:
        return vf
    
    #||||||||||||||||ELIMINAR|||||||||||||||||||||
    
@routes_Producto.route('/clearCat', methods=['GET'] ) 
def eliminar_Product(id):
    prod = Productos.query.get(id)
    db.session.delete(prod)
    db.session.commit()
    return jsonify(Productos_Schema.dump(cli)) 

#||||||||||||||||ACTUALIZAR|||||||||||||||||||||

@routes_Producto.route('/updateClientes', methods=['POST'] )
def actualizar_Prod():
    id = request.json['id']
    new_prod = request.json['N_Product']
    Descripcion = request.json['Descripcion']
    updateProd = Productos.query.get(id)
    updateProd.nameClie = new_prod
    updateProd.descripProd = Descripcion
    db.session.commit()
    return redirect('/Productos')