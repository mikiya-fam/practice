from datetime import datetime
from database import db


class Member(db.Model):

    __tablename__ = 'T_MEMBER'

    member_id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(10))
    first_name = db.Column(db.String(10))
    sex = db.Column(db.String(1))
    user_id = db.Column(db.String(10))
    password = db.Column(db.String(10))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    delete = db.Column(db.String(1))
