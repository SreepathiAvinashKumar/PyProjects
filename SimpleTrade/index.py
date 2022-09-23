from urllib import response
import requests
import json

# parameters = {

# }

res = requests.get("https://jsonplaceholder.typicode.com/posts/")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(res.json()[0]['title'])
