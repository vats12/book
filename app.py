from flask import *
from flask_cors import CORS
from flask_restful import Resource, Api
from api import create_api

app = Flask(__name__)
app.secret_key = "Book keeping"  
CORS(app)
api = Api(app)
create_api(api)

if __name__ == '__main__':
    app.run(port='8080', host='0.0.0.0', debug=True)