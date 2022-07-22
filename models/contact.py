from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, fullname, phone, email):
        self.fullname = fullname
        self.phone = phone
        self.email = email
