from twilio.rest import Client 
 
account_sid = 'AC81702a0bd87f8c5192713f9dda783b1a' 
auth_token = '8371e18d3f1c9eee23ed1d8c9a1500a1' 
client = Client(account_sid, auth_token) 
 
def send_love():
    message = client.messages.create( 
      from_='whatsapp:+14155238886',
      body='hey Captain I just automated this message \n \
        It run with twilio API \n \
        it will be sending msg to you after every 1 hour.\n \
        just ignore \n \
        if you get it send a screenshot.\
        happy hack its CLINTON THE CHIENJAH....  😍😍😍 \n \
        I think we can build somthing cool with this API.....are you in',
        to='whatsapp:+254797324006' 
                          )
def send_love_captain():
  message = client.messages.create( 
      from_='whatsapp:+14155238886',
      body='hey Captain I just automated this message \n \
        It run with twilio API \n \
        it will be sending msg to you after every 1 hour.\n \
        just ignore \n \
        if you get it send a screenshot.\
        happy hack its CLINTON THE CHIENJAH....  😍😍😍 \n \
        I think we can build somthing cool with this API.....are you in',
        to='whatsapp:+254704209395' 
        )

 
  print(message.sid)