from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask_sqlalchemy import SQLAlchemy

routes_home = Blueprint("routes_home", __name__)

@routes_home.route("/index",  methods=['GET'])
def index():
    titulo = "Pagina pricipal"
    return render_template('/main/index.html', titles=titulo)

@routes_home.route("/productos",  methods=['GET'])
def productos():
    titulo = "Pagina Productos"
    return render_template('/main/product.html', titles=titulo)

@routes_home.route("/contacto",  methods=['GET'])
def contacto():
    titulo = "Pagina contacto"
    return render_template('/main/contact.html', titles=titulo)


