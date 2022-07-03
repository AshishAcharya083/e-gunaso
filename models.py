from app import  db
from datetime import datetime


class Complaint(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    creator_id = db.Column(db.String(50))
    description = db.Column(db.String(300))
    municipality_name = db.Column(db.String(50))
    ward_no = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self):
        super().__init__()


