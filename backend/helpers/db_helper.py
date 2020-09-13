from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.database_models import Word, Company, Job


class DBHelper():
    engine = create_engine("postgres://ciarannolan@localhost/rats")
    Session = sessionmaker(bind=engine)
    session = Session()

    def insertCompany(self,companyName):
        company = Company(companyName)
        self.session.add(company)
        self.session.commit()

    def insertJob(self,companyName):
        company = Company(companyName)
        self.session.add(company)
        self.session.commit()