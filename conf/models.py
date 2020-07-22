from datetime import datetime
from conf.database import db


class Member(db.Model):

    __tablename__ = 'T_MEMBER'

    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(10))
    first_name = db.Column(db.String(10))
    sex = db.Column(db.String(1))
    user_id = db.Column(db.String(10))
    password = db.Column(db.String(10))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    delete_flag = db.Column(db.String(1))

class Schedule(db.Model):

    __tablename__ = 'T_SCHEDULE'
    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    event_name = db.Column(db.String(20))
    place = db.Column(db.String(20))
    comment = db.Column(db.String(500))
    member_id = db.Column(db.Integer)
    member_count = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    delete_flag = db.Column(db.String(1))
