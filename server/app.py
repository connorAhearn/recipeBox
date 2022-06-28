from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys

# Allows us to import api from another folder
sys.path.insert(1, '../spoonacular')
from api import get_ingredients

app = Flask(__name__)

# CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
from flask import Response
@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()

# Homepage route
@app.route("/")
@cross_origin()
def index():
    return 'hello world'

# Basic API call for getting ingredients from an example URL
@app.route("/ingredients")
@cross_origin()
def ingredients():
    return {'ingredients': get_ingredients('https://www.sipandfeast.com/pasta-alla-norcina/')}

# Essential API call for returning ingredients for provided URL
@app.route("/recipe", methods=['GET', 'POST'])
@cross_origin()
def recipe():
    content = request.json
    url = content['url']
    return {'ingredients': get_ingredients(url)}

if __name__ == '__main__':
    app.run(debug=True)