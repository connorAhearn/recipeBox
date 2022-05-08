from flask import Flask

import sys

# Allows us to import api from another folder
sys.path.insert(1, '../spoonacular')
from api import get_ingredients

app = Flask(__name__)

# Homepage route
@app.route("/")
def index():
    return 'hello world'

# Basic API call for getting ingredients from a provided URL
# TODO: Take a provided url as input & insert into the get_ingredients function
@app.route("/ingredients")
def ingredients():
    return {'ingredients': get_ingredients('https://www.sipandfeast.com/pasta-alla-norcina/')}


if __name__ == '__main__':
    app.run(debug=True)