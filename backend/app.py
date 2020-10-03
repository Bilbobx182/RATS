from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from helpers.jobsearch import JobSearch
from flask_graphql import GraphQLView
from models.schema_objects import get_schema

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/get_words_indeed', methods=['POST'])
def user():
    # Usually use NGINX or something like it to do this, but for the sake of getting this out. Use this approach.
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()

    if request.method == 'POST':
        try:
            js = JobSearch(request.json['title'])
            data = js.search()
            print(data)
            return add_cors_headers(jsonify(data))
        except Exception as e:
            return jsonify({
                'labels': ['EXCEPTION OCCURRED PLEASE TRY AGAIN'],
                'datasets': [{
                    'data': [500]
                }]})


@cross_origin()
@app.route('/')
def index():
    return jsonify({"Pong": "200"})


def _build_cors_prelight_response():
    # SO https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.debug = True
    db = SQLAlchemy(app)
    app.run(host='0.0.0.0')

    # TODO Deprecated GraphQL config
    # app.add_url_rule(
    #     '/graphql-api',
    #     view_func=GraphQLView.as_view(
    #         'graphql',
    #         schema=get_schema(),
    #         graphiql=True
    #     )
    # )
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ciarannolan@localhost/rats'
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
