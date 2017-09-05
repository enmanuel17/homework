#enmanuel hernadez
#program to send text messages via python and using twilio
#parts of code are from the udacity learning course

from twilio.rest import Client

#Account SID and Auth token from twilio.
account_sid = "AC4ff4279d8327c941fdb7304563951dd0"
auth_token = "b623f37365163366ec0b42c2a7e24e63"
client = Client(account_sid, auth_token)


message = client.messages.create(
	body = "Hello my name is enamnuel and this is a test message",
	to= "6464503639",      #allow to text number from twilio.
	from_="18482299501") #my twilio phone number

print message.sid 
