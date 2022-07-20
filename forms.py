from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Email,DataRequired,InputRequired

from models import State


class ComplaintForm(FlaskForm): 


    # def state_choices(): 
    #     return State.query.all()

    title = StringField('title',validators=[InputRequired()])
    description = StringField('description',validators=[InputRequired()])
    # state_id = QuerySelectField('state_id',validators=[InputRequired()])
    sate_id = IntegerField('state',validators=[InputRequired()])
    municipality_id = IntegerField('muncipality',validators=[InputRequired()])
    ward_id = IntegerField('ward',validators=[InputRequired()])
    status = IntegerField('status',validators=[InputRequired()])
    created_by = IntegerField('created_by',validators=[InputRequired()])
    submit = SubmitField('Add Complaint')


class User(FlaskForm): 
    pass
