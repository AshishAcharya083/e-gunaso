from app import  db
from datetime import datetime


class Complaint(db.model):
    __table_name__ = 'complaint'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    creator_id = db.Column(db.String(50))
    description = db.Column(db.String(300))
    municipality_name = db.Column(db.String(50))
    ward_no = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(), db.ForeignKey("user.id"))

    def __init__(self):
        super().__init__()


class User(db.model):
    __table_name__ = 'user'
    id: db.Column(db.Integer, primary_key=True)
    first_name: db.Column(db.String(15))
    email: db.Column(db.String(20))
    password_hash: db.Column(db.String())
    address: db.Column(db.String(50))


