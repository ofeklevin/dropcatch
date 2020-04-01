import requests
import xmltodict
import time
import xml.etree.ElementTree as ET
import json


def check_domain(domain):
    available = False

    payload = {'key': ApiKey,
               'command': 'search',
               'domain0': domain,
               'show_price': '1'
               }

    try:
        response = requests.get(URL, payload)
        print(response.text)
        available = '<Available>yes</Available' in response.text

    except requests.exceptions.RequestException as e:
        print(e)

    return available


def register_domain(domain):
    answer = ""

    payload = {'key': ApiKey,
               'command': 'register',
               'domain': domain,
               'duration': '1'
               }
    try:
        response = requests.get(URL, payload)
        answer = response.text
    except requests.exceptions.RequestException as e:
        answer = "e"

    return (answer)


# Production
URL = "https://api.dynadot.com/api3.xml"
ApiKey = "api_key" # Enter your API key

targeted_domain = "example.com" 
attempt = 0
while True:
    attempt = attempt + 1
    print("Checking Domain " + targeted_domain)
    print("Attempt number " + str(attempt))
    result = check_domain(targeted_domain)
    print(result)
    if result:
        print("Registering Domain " + targeted_domain)
        print(register_domain(targeted_domain))

print("Process over - domain may be bought")
