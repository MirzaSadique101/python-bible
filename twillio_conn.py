from twilio.rest import Client
from config import account_sid,auth_token,phone

def setup_twilio_conn(account_sid,auth_token,phone):
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client,quote):
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=quote,      
                              to='whatsapp:{}'.format(phone)
                          ) 
    return message.sid

client = setup_twilio_conn(account_sid,auth_token,phone)