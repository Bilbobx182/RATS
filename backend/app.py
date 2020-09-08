from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from backend.models.schema_objects import get_schema
from flask import request
from flask import jsonify

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
        print(request.json['title'])

        data = {
            'labels': [
                'Hello',
                'Ciaran',
                'World'
            ],
            'datasets': [{
                'data': [300, 50, 100],
                'backgroundColor': [
                    '#42a5f5','#ffca28', '#ff7043', '#ab47bc', '#26c6da', '#66bb6a', '#ec407a'
                ],
                'hoverBackgroundColor': [
                    '#90caf9','#fff59d', '#ffab91', '#ce93d8', '#80deea', '#a5d6a7', '#f48fb1'
                ]
            }]}
        return jsonify(data)


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
