#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "ddfcfad918b14acef63d82f79a0d4e20"
api_app_key = "013169b6b9c9c1f12fa85d6feb5aa0c9bb3fc206"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:105594-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)
# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
