# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializing our app
app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)

# Configs


# Configs
# Replace the user, password, hostname and database according to your configuration information

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ciarannolan@localhost/rats'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Modules
db = SQLAlchemy(app)

# Modules
# SQLAlchemy will be initiated here

# Models
# Our relations will be setup here

# Schema Objects
# Our schema objects will go here

# Routes
# Our GraphQL route will go here

@app.route('/')
def index():
    return 'Welcome to Book Store Api'
if __name__ == '__main__':
     app.run()