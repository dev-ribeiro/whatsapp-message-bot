import requests
from dotenv import *
import pandas as p

config = dotenv_values('.env')
instance = config['ULTRA_MSG_INSTANCE_ID']
token = config['ULTRA_MSG_TOKEN']

url = "https://api.ultramsg.com/{instance}/messages/chat".format(instance = instance)
default_message = "Hello World"
contacts = p.read_csv('datasets/contacts.csv')

for index, row in contacts.iterrows():
    message = row['message'] if row['message'] != "undefined" else default_message
    contact = row['phone']

    payload = "token={token}&to=+{contact}&body={message}".format(token = token,    contact = contact, message = message)

    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
