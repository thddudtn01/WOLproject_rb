import requests
import json
URL = "http://ssl305.herokuapp.com/"
resp = requests.get(URL)
print(resp.status_code)
print(json.loads(resp.text)["return"])