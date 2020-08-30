from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from backend.models.database_models import Location, Job, Company, Word
import graphene


class LocaitonObject(SQLAlchemyObjectType):
    class Meta:
        model = Location
        interfaces = (graphene.relay.Node,)


class CompanyObject(SQLAlchemyObjectType):
    class Meta:
        model = Company
        interfaces = (graphene.relay.Node,)


class WordObject(SQLAlchemyObjectType):
    class Meta:
        model = Word
        interfaces = (graphene.relay.Node,)


class JobObject(SQLAlchemyObjectType):
    class Meta:
        model = Job
        interfaces = (graphene.relay.Node,)


class Company_Location(graphene.Union):
    class Meta:
        types = (Company, Location)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    search = graphene.List(Company_Location, q=graphene.String())  # List field for search results

    all_companies = SQLAlchemyConnectionField(CompanyObject)
    all_locations = SQLAlchemyConnectionField(LocaitonObject)
    all_jobs = SQLAlchemyConnectionField(JobObject)
    all_words = SQLAlchemyConnectionField(LocaitonObject)

    def resolve_search(self, info, **args):
        q = args.get("q")  # Search query

        # Get queries
        bookdata_query = LocaitonObject.get_query(info)
        author_query = Author.get_query(info)

        # Query Books
        books = bookdata_query.filter((BookModel.title.contains(q)) |
                                      (BookModel.isbn.contains(q)) |
                                      (BookModel.authors.any(AuthorModel.name.contains(q)))).all()

        # Query Authors
        authors = author_query.filter(AuthorModel.name.contains(q)).all()

        return authors + books  # Combine lists


def get_schema():
    return graphene.Schema(query=Query, types=[Job, Company, Location, Word, Company_Location])
