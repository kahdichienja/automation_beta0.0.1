from twilio.rest import Client 
 
account_sid = 'AC81702a0bd87f8c5192713f9dda783b1a' 
auth_token = '04bfe1e6dd53e03b39b14e4da302f005' 
client = Client(account_sid, auth_token) 
 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hey be dont worry its client if you get this msg screenshot and sent it to my number',      
                              to='whatsapp:+254797324006' 
                          )

 
    print(message.sid)