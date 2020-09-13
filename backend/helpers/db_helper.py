from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.database_models import Word, Company, Job
from datetime import datetime


class DBHelper():
    engine = create_engine("postgres://ciarannolan@localhost/rats")
    Session = sessionmaker(bind=engine)
    session = Session()
    today = datetime.today().strftime('%Y-%m-%d')

    def insertCompany(self,companyName):
        company = Company(companyName)
        self.session.add(company)
        self.session.commit()

    def insertJob(self,job):
        job = Job(job,company_id,content,self.today)
        self.session.add(job)
        self.session.commit()