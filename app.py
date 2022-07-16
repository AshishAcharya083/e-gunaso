from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from complains.blueprint import complains

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(complains,url_prefix = '/complains')

db = SQLAlchemy(app)


@app.route('/')
def index(): 
    return render_template("index.html")
