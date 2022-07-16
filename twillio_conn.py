from twilio.rest import Client
import os
 
account_sid = os.environ.get('TWILLIO_ACCOUNT_SID') 
auth_token = os.environ.get('TWILLIO_ACCOUNT_TOKEN')
client = Client(account_sid, auth_token) 
phone = os.environ.get('PHONE_NUMBER')
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:{}'.format(phone)
                          ) 
 
print(message.sid)