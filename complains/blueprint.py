from models import Complaint,db
from flask import Blueprint,render_template



complains = Blueprint("complains",__name__,template_folder="templates")


@complains.route('/')
def complains_list():
    return render_template("complains.html")

