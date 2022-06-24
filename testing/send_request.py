import requests
import pprint
res = requests.post('http://localhost:5000/recipe', json={"url":"https://www.sipandfeast.com/pasta-alla-norcina/"})
if res.ok:
    print(res.content)