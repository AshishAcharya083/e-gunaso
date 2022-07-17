from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from complains.blueprint import complains
from database import db
from models import Complaint


# db = SQLAlchemy(app)



def register_extension(app): 
    db.init_app(app)


def create_app(config): 
    app = Flask(__name__)
    app.config.from_object(config)
    register_extension(app)
    return app

app = create_app(Config)


app.register_blueprint(complains,url_prefix = '/complains')



@app.route('/')
def index(): 
    result = Complaint.query.all()
    print(result[0].title)
    return render_template("index.html")

