from twilio.rest import Client
account_sid = 'AC6dd9388d418f5ffe2371e016ecc2ca0f' # Add your Twilio Account's SID
auth_token = '0f3399db9ccd000eef8c635de49f6a26' # Add your Twilio Account's Auth Token
client = Client(account_sid, auth_token)
def send_rem(date,rem):
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='*REMINDER* '+date+'\n'+rem,
  to='whatsapp:+918277164818' # Add your WhatsApp No. here
)
print(message.sid) 
