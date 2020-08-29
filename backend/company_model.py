# Modules
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from backend.app import db
# Models


class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)

    def __init__(self, location_id,country,state,city):
      self.location_id = location_id
      self.country = country
      self.state = state
      self.city = city

    def __repr__(self):
        return '' % self.location_id

class Word(db.Model):
    __tablename__ = 'word'
    word_id = db.Column(db.String, primary_key=True)
    jobs_fk = db.ARRAY(db.String, nullable=True)
    frequency = db.Column(db.Integer,nullable=True)

    def __init__(self, word_id, jobs_fk):
        self.word_id = word_id
        self.jobs_fk = jobs_fk

    def __repr__(self):
        return '' % self.word_id



class Company(db.Model):
    __tablename__ = 'company'

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    location_id = db.Column(db.Integer,db.ForeignKey('location.location_id'), nullable=True)
    jobs_fk = db.Column(db.String, nullable=True)

    books = db.relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '' % self.id




class Job(db.Model):
    __tablename__ = 'job'

    job_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer,db.ForeignKey('company.company_id'), nullable=True)
    locations_id = db.Column(db.String, nullable=True)
    contents = db.Column(db.String, nullable=True)
    pay = db.Column(db.String, nullable=True)
    date_posted = db.Column(db.String, nullable=True)
    has_pension = db.Column(db.Boolean, nullable=True)
    has_healthcare = db.Column(db.Boolean, nullable=True)
    has_stock = db.Column(db.Boolean, nullable=True)

    def __init__(self, job_id, company_id, location_id,contents,pay,date_posted,has_pension, has_healthcare, has_stock):
      self.job_id = job_id
      self.company_id = company_id
      self.locations_id = location_id
      self.contents = contents
      self.pay = pay
      self.date_posted = date_posted
      self.has_pension = has_pension
      self.has_stock = has_stock
      self.has_healthcare = has_healthcare


    def __repr__(self):
        return '' % self.id