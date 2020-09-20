from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask import request
from flask import jsonify

from models.schema_objects import get_schema
from helpers.jobsearch import JobSearch

app = Flask(__name__)

app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=get_schema(),
        graphiql=True
    )
)


@app.route('/get_job_words', methods=['POST'])
def user():
    if request.method == 'POST':
        try:
            js = JobSearch(request.json['title'])
            data = js.search()
            print(data)
            return jsonify(data)
        except Exception as e:
            return jsonify({
        'labels': ['EXCEPTION OCCURRED PLEASE TRY AGAIN'],
        'datasets': [{
            'data': [500]
        }]})





@app.route('/')
def index():
    return 'Welcome to the future of jobs and CVs'


if __name__ == '__main__':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ciarannolan@localhost/rats'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)
    app.run(host='0.0.0.0')
