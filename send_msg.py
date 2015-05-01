from twilio.rest import TwilioRestClient

import json

data = []
with open('items.jl') as f:
    for line in f:
        data.append(json.loads(line))

title = 'Dining Hall summary for today.'
message = ""
for item in data:
    if len(item['favor']) > 0:
        message = message + item['hall_name'] + \
            " has " + ", ".join(item['favor']) + \
            ". Here is the link for the full menu \n" + item['link'] + "\n"

ACCOUNT_SID = "ACd5403d503d5bac5f58888a326138fe05"
AUTH_TOKEN = "e3d0325d0f5375f712de3f0d9e9e75d7"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


if len(message) > 0:
    client.messages.create(
        to="8325062758",
        from_="+19787679888",
        body=message
    )

else:
    message = "Nothing is good for today.\n"
    message = message + "Please checkout the following websites \
to see if there are sth you like.\n"
    for item in data:
        message = message + item['hall_name'] + "\n" + item['link'] + "\n"
    message = message + "Email me your favorite\
 dishes so that I can add them to the list."
    client.messages.create(
        to="8325062758",
        from_="+19787679888",
        body=message
    )

# put your own credentials here
