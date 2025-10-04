from flask import Flask,request,jsonify 
from flask_sqlalchemy import SQLAlchemy
from config import Development
app=Flask(__name__)
app.config.from_object(Development)
db=SQLAlchemy()
db.init_app(app)
def create_app():
    
    
    
   
    with app.app_context():
        from app import models
        db.create_all()
    from app.routes import routing
    routing(app)
    return app
