import requests

# Secrets
from config import API_KEY

EXTRACT_RECIPE_API_URL = 'https://api.spoonacular.com/recipes/extract'

# Adding request parameters to a URL
def append_parameter(url, parameter_name, parameter):
    return url + '&' + parameter_name + '=' + parameter

# Main method of the module
def get_ingredients(url):

    # Getting recipe info from spoonacular for the provided url
    request_url = EXTRACT_RECIPE_API_URL + '?apiKey=' + API_KEY
    request_url = append_parameter(request_url, 'url', url)
    response = requests.get(request_url).json()

    # Cleaning up the result & returning it
    extended_ingredients = response['extendedIngredients']
    basic_ingredients = [ingredient['name'] for ingredient in extended_ingredients]
    return basic_ingredients