from flask import Flask,request,jsonify 
from config import Development
from app.routes import routing

def create_all():
    app=Flask(__name__)
    app.config.from_object(Development)
    
    routing(app)
    return app
