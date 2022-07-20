from models import Complaint,db
from flask import Blueprint,render_template,request,redirect,Response
from forms import ComplaintForm


complains = Blueprint("complains",__name__,template_folder="templates")


@complains.route('/')
def complains_list():
    return render_template("complains.html")



@complains.route('/addcomplaint',methods=["POST"])
def add_complaint(): 
    if request.method == "POST":
        print(request.form["title"])
        return Response(status=201)
        
        

@complains.route('/result')
def complains_response():
    return render_template("result.html")



@complains.route('/complaint_modal')
def complaint_modal(): 
    form = ComplaintForm()
    return render_template("complaint_modal.html",form=form)