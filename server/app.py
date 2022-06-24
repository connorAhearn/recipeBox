from flask import Flask, request

import sys

# Allows us to import api from another folder
sys.path.insert(1, '../spoonacular')
from api import get_ingredients

app = Flask(__name__)

# Homepage route
@app.route("/")
def index():
    return 'hello world'

# Basic API call for getting ingredients from an example URL
@app.route("/ingredients")
def ingredients():
    return {'ingredients': get_ingredients('https://www.sipandfeast.com/pasta-alla-norcina/')}

# Essential API call for returning ingredients for provided URL
@app.route("/recipe", methods=['GET', 'POST'])
def recipe():
    content = request.json
    url = content['url']
    return {'ingredients': get_ingredients(url)}

if __name__ == '__main__':
    app.run(debug=True)