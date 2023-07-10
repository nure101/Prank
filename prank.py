#prject ready 
import os
from twilio.rest import Client
from time import sleep


# Retrieve Twilio account SID and authentication token from environment variables
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
my_number = os.environ.get('my_number')
twilio_number = os.environ.get('my_twilio_number')
client = Client(account_sid, auth_token)

client.messages.create(
                to = my_number,
                from_ = twilio_number,
            # max char Twilio can send: 72
                body = "This is your good friend Nure. perpare for some trolling"
            )

with open('/Users/nuremo/Desktop/projects/project_everbridge/bees.txt','r') as f:
    f = f.readlines()
    for i in f:
        client.messages.create(
                to = my_number,
                from_ = twilio_number,
            # max char Twilio can send: 72
                body = i
            )