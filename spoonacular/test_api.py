import unittest

# Module we're testing
import api

class TestApi(unittest.TestCase):

    # Basic test
    def test_append_parameter(self):
        url = 'https://google.com'
        parameter_name = 'apiKey'
        parameter = '123b'

        expected = url + '&' + parameter_name + '=' + parameter
        actual = api.append_parameter(url, parameter_name, parameter)

        self.assertEqual(expected, actual)


    # Testing the API with a recipe I'm familiar with
    def test_get_ingredients(self):
        expected = [
            'rigatoni',
            'baby bella mushrooms',
            'bulk mild sausage',
            'olive oil',
            'onion',
            'garlic',
            'wine',
            'heavy cream',
            'reserved pasta water',
            'nutmeg',
            'pecorino romano',
            'salt and pepper'
        ]
        actual = api.get_ingredients('https://www.sipandfeast.com/pasta-alla-norcina/')

        for ingredient in expected:
            self.assertTrue(ingredient in actual)

        self.assertEqual(len(expected), len(actual))


if __name__ == '__main__':
    unittest.main()