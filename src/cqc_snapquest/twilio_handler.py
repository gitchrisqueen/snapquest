from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "xxxxxx")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "xxxxxx")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "xxxxxx")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to, message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )
