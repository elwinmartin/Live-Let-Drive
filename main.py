import yaml
import requests

# Load Config 
with open("config.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

# call request for apartment data


# This should be moved to config probably
url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=&destinations=&key='

url = http://www.example.com
# Sample request
r = requests.get(url)
response_json = r.content

# Decode json from google api

# Parse for time and distance

# Implement filter here
