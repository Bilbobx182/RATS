from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from backend.models.database_models import Location ,Job, Company, Word
import graphene

class LocaitonObject(SQLAlchemyObjectType):
   class Meta:
       model = Location
       interfaces = (graphene.relay.Node, )

class CompanyObject(SQLAlchemyObjectType):
   class Meta:
       model = Company
       interfaces = (graphene.relay.Node, )

class WordObject(SQLAlchemyObjectType):
   class Meta:
       model = Word
       interfaces = (graphene.relay.Node, )

class JobObject(SQLAlchemyObjectType):
   class Meta:
       model = Job
       interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_companies = SQLAlchemyConnectionField(CompanyObject)
    all_locations = SQLAlchemyConnectionField(LocaitonObject)
    all_jobs = SQLAlchemyConnectionField(JobObject)
    all_words = SQLAlchemyConnectionField(LocaitonObject)

def get_schema():
    return graphene.Schema(query=Query)