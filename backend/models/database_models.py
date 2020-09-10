from sqlalchemy.orm import relationship, backref

from backend.extensions import db


class Location(db.Model):
    __tablename__ = 'location'
    __table_args__ = {'extend_existing': True}

    location_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)

    def __init__(self, location_id, country, state, city):
        self.location_id = location_id
        self.country = country
        self.state = state
        self.city = city

    def __repr__(self):
        return '' % self.location_id


class Word(db.Model):
    __tablename__ = 'word'
    __table_args__ = {'extend_existing': True}

    word_id = db.Column(db.String, primary_key=True)
    jobs_fk = db.Column(db.Integer)
    frequency = db.Integer(db.Integer)

    def __init__(self, word_id, jobs_fk):
        self.word_id = word_id
        self.jobs_fk = jobs_fk

    def __repr__(self):
        return '' % self.word_id


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    location = relationship(Location, backref=backref('companies', uselist=True))

    jobs_fk = db.Column(db.String)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '' % self.id


class Job(db.Model):
    __tablename__ = 'job'
    __table_args__ = {'extend_existing': True}

    job_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    company = relationship(Company, backref=backref('companies', uselist=True))

    locations_id = db.Column(db.String)
    contents = db.Column(db.String)
    pay = db.Column(db.String)
    date_posted = db.Column(db.String)
    has_pension = db.Column(db.Boolean)
    has_healthcare = db.Column(db.Boolean)
    has_stock = db.Column(db.Boolean)

    def __init__(self, job_id, company_id, location_id, contents, pay, date_posted, has_pension, has_healthcare,
                 has_stock):
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
