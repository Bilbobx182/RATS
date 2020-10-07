from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from helpers.jobsearch import JobSearch

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def _build_cors_prelight_response():
    # SO https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    print(f'returing {response}')
    return response


@cross_origin()
@app.route('/get_job_words',methods = ['OPTIONS','POST'])
def get_job_words():
    if request.method == "OPTIONS":
        print("HELLO WORLD")
        return _build_cors_prelight_response()
    # Usually use NGINX or something like it to do this, but for the sake of getting this out. Use this approach.
    try:
        js = JobSearch(request.json['title'])
        data = js.search()
        resp = jsonify(data)
        print(resp)
        return (resp)
    except Exception as e:
        return jsonify({
                'labels': ['EXCEPTION OCCURRED PLEASE TRY AGAIN'],
                'datasets': [{'data': [500]}]}).headers.add('Access-Control-Allow-Origin', '*')


@cross_origin()
@app.route('/')
def index():
    return jsonify({"Pong": "200"})


if __name__ == '__main__':
    app.debug = True
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
