import yaml
import requests
import sys # Assuming we use sys.arg, could be deprecated
try:
    import json
except ImportError:
    import simplejson as json


# Load Config 
with open("config.yml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

quit() #Testing

# yaml access looks like doc["treeroot"]

# Load CLI Args
url_encoded_args = map() 
try:
    origin, destination, key = sys.argv
except IndexError as exc:
	print(exc)

# call request for apartment data
	# This should be moved to config probably
url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'.format(origin,destination,key)

print(url_base)

url = http://www.example.com
# Sample request
r = requests.get(url)
response_json = r.content

# Decode json from google api
response_dict = json.loads(response_json)
# Parse for time and distance

# Implement filter here
