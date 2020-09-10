from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from backend.models.schema_objects import get_schema
from flask import request
from flask import jsonify

from backend.helpers.jobsearch import JobSearch

app = Flask(__name__)

# Routes
# Our GraphQL route will go here
app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=get_schema(),
        graphiql=True
    )
)


@app.route('/dummy_words', methods=['POST'])
def user():
    if request.method == 'POST':
        # print(request.json['title'])
        # js = JobSearch(request.json['title'])
        # data = js.search()
        # return jsonify(data)
        labels =['hello','world','pocari','weeb','waifu','ciaran','wee','dying','hey','im','sorry']
        data = [0,1,2,3,4,5,6,7,8,9]

        hello = {
            'labels': [
                'Hello',
                'Ciaran',
                'World'
            ],
            'datasets': [{
                'data': [300, 50, 100]
            }]}

        rest = {
            'labels': labels,
            'datasets': [{
                'data': data
            }]}
        return jsonify(rest)


@app.route('/')
def index():
    return 'Welcome to the future of jobs and CVs'


if __name__ == '__main__':
    # initializing our app
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ciarannolan@localhost/rats'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)
    app.run()

#    from backend.company_model import Location
# aman = Location(2, country='England', state='London', city='Stratford')
# db.session.add(aman)
# db.session.commit()
