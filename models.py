from database import  db
from datetime import datetime
import enum


class User(db.Model):
    __table_name__ = 'user'
    user_id= db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(15))
    email= db.Column(db.String(20))
    password_hash= db.Column(db.String())
    address= db.Column(db.String(50))


class Status(enum.Enum):
    selected = 'selected'
    in_process = 'in process'
    done = 'done'
    rejected = 'rejected'
    pending = 'pending'


class Complaint(db.Model):
    __table_name__ = 'complaint'
    complaint_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    creator_id = db.Column(db.String(50))
    description = db.Column(db.String(300))
    state = db.Column(db.String(15))
    municipality_name = db.Column(db.String(50))
    ward_no = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Enum(Status, values_callable=lambda x: [str(member.value) for member in Status]))
    created_by = db.Column(db.String(), db.ForeignKey("user.user_id"))


class Ward(db.Model):
    __table_name__ = 'ward'
    ward_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    number = db.Column(db.Integer)
    municipality_id = db.Column(db.Integer(), db.ForeignKey("municipality.mun_id"))


class Municipality(db.Model):
    __table_name__ = "municipality"
    mun_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    state_id = db.Column(db.Integer, db.ForeignKey("state.state_id"))


class State(db.Model):
    __table_name__ = "state"
    state_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))













