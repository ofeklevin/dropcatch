import requests
import xmltodict
import time
import xml.etree.ElementTree as ET
import json
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from string import ascii_lowercase
import random


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
ApiKey = "DYNADOT_API_KEY" # Change this to your dynadot API key
tld = "com" # TLD to search for

while True:
    name = ''.join(random.choice(ascii_lowercase) for i in range(4))
    domain = str(name) + "." + str(tld)
    check = check_domain(domain)
    if check:
        print("Buying domain" + domain)
        register_domain(domain)
