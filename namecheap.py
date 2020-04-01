import requests
import xmltodict
import time
import xml.etree.ElementTree as ET
import json
from urllib3.exceptions import HTTPError as BaseHTTPError


def check_domain(domain):
    available = False

    payload = {'ApiUser': 'API_username', # Add your API Username
               'ApiKey': ApiKey,
               'UserName': 'username', # Add your dynadot Usermame
               'Command': 'namecheap.domains.check',
               'ClientIp': IP,
               'DomainList': domain
               }

    try:
        response = requests.post(URL, payload)

        root = ET.fromstring(response.text)

        for child in root:
            if "CommandResponse" in child.tag:
                for child2 in child:
                    if "DomainCheckResult" in child2.tag:
                        print(child2.attrib)
                        # If i change this that it will insert child2.attrib.get('Domain')
                        # into a dict I can make this good for calling multiple domains, but for now its fine.
                        available = (child2.attrib.get('Available') == 'true')

    except requests.exceptions.RequestException as e:
        print(e)

    return available


def register_domain(domain):
    answer = ""

    payload = {'ApiUser': 'API_username', # Add your API Username
               'ApiKey': ApiKey,
               'UserName': 'username',  # Add your dynadot Usermame
               'ClientIp': IP,
               'Command': 'namecheap.domains.create',
               'DomainName': domain,
               'Years': '1',
               'RegistrantFirstName': 'first_name',
               'RegistrantLastName': 'last_name',
               'RegistrantAddress1': 'address',
               'RegistrantCity': 'city',
               'RegistrantStateProvince': 'province',
               'RegistrantPostalCode': 'postal_code',
               'RegistrantCountry': 'country',
               'RegistrantPhone': 'phone_number', # Ex. +972.581111111
               'RegistrantEmailAddress': 'email_address',
               'TechFirstName': 'first_name',
               'TechLastName': 'last_name',
               'TechAddress1': 'address',
               'TechCity': 'city',
               'TechStateProvince': 'province',
               'TechPostalCode': 'postal_code',
               'TechCountry': 'country',
               'TechPhone': 'phone_number',
               'TechEmailAddress': 'email_address',
               'AdminFirstName': 'first_name',
               'AdminLastName': 'last_name',
               'AdminAddress1': 'address',
               'AdminCity': 'city',
               'AdminStateProvince': 'province',
               'AdminPostalCode': 'postal_code',
               'AdminCountry': 'country',
               'AdminPhone': 'phone_number',
               'AdminEmailAddress': 'email_address',
               'AuxBillingFirstName': 'first_name',
               'AuxBillingLastName': 'last_name',
               'AuxBillingAddress1': 'address',
               'AuxBillingCity': 'city',
               'AuxBillingStateProvince': 'province',
               'AuxBillingPostalCode': 'postal_code',
               'AuxBillingCountry': 'country',
               'AuxBillingPhone': 'phone_number',
               'AuxBillingEmailAddress': 'email_address',
               'AddFreeWhoisguard': 'yes',
               'WGEnabled': 'yes'
               }
    try:
        response = requests.post(URL, payload)
        answer = response.text
    except requests.exceptions.RequestException as e:
        answer = "e"

    return (answer)


# Production 
URL = "https://api.namecheap.com/xml.response"
ApiKey = "api_key"

# Sandbox - Use this for testing if you have a sandbox account
# URL = "https://api.sandbox.namecheap.com/xml.response"
# ApiKey = "api_key" # Enter your sandbox API key here
IP = '0.0.0.0' # Enter your public IPV4 address
targeted_domain = "example.com" # Domain to try and catch
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
    time.sleep(10)

print("Process over - domain may be bought")
