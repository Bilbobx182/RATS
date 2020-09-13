from sqlalchemy.orm import relationship, backref
from backend.extensions import db


class Word(db.Model):
    __tablename__ = 'word'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)
    jobs_fk = db.Column(db.Integer)
    frequency = db.Column(db.Integer)

    def __init__(self,word, jobs_fk, frequency):
        self.word = word
        self.jobs_fk = jobs_fk
        self.frequency = frequency

    def __repr__(self):
        return '' % self.word_id


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '' % self.id


class Job(db.Model):
    __tablename__ = 'job'
    __table_args__ = {'extend_existing': True}

    job_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    company = relationship(Company, backref=backref('companies', uselist=True))
    contents = db.Column(db.String)
    date_posted = db.Column(db.String)

    def __init__(self, job_id, company_id, contents, date_posted):
        self.job_id = job_id
        self.company_id = company_id
        self.contents = contents
        self.date_posted = date_posted


    def __repr__(self):
        return '' % self.id
