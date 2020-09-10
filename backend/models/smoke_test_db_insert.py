from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.database_models import Word, Location, Company, Job

engine = create_engine("postgres://ciarannolan@localhost/rats")
Session = sessionmaker(bind=engine)
session = Session()

# word = Word("Java",1,1)
# session.add(word)

# location = Location(3,'United States','San Diego','California')
# session.add(location)

# dell = Company('Dell',1,'1')
# session.add(dell)
# session.commit()

#
# indeed_job = Job(3,1,1,'data some code goes here',"40000¢",'01-01-0000',True,False,False)
# session.add(indeed_job)
# session.commit()
