from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma




from rutas import routes_index
