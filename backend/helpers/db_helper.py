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

    def insertJob(self,job_title,company_id,content):
        job = Job(job_title,company_id,content,self.today)
        self.session.add(job)
        self.session.commit()

    # def insertWord(self,word,job_fk,frequency):
    #     objects = [
    #         Word(word=word,jobs_fk=job_fk,frequency=fre),
    #         User(name="u2"),
    #         User(name="u3")
    #     ]
    #     s.bulk_save_objects(objects)
    #     s.commit()
    #     word = Word(word,job_fk,frequency)
    #     self.session.add(word)
    #     self.session.commit()