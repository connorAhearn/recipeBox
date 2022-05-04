import requests

# Secrets
from config import API_KEY

EXTRACT_RECIPE_API_URL = 'https://api.spoonacular.com/recipes/extract'

def append_parameter(url, parameter_name, parameter):
    return url + '&' + parameter_name + '=' + parameter

request_url = EXTRACT_RECIPE_API_URL + '?apiKey=' + API_KEY
request_url = append_parameter(request_url, 'url', 'https://www.sipandfeast.com/pasta-alla-norcina/')

response = requests.get(request_url).json()

for ingredient in response['extendedIngredients']:
    print(ingredient['name'])