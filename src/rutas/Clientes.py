from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Clientes import Clientes

routes_Admin = Blueprint("routes_Clientes", __name__)


@routes_Clientes.route('/indexClientes', methods=['GET'] )
def indexClientes():
    
    return render_template('/main/Clientes.html')