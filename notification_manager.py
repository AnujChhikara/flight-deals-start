from twilio.rest import Client
account_sid = "AC5910bc68f4de1ee8052f733a7c37cd81"
auth_token = "f5ebe0c60f6dbb097cfcbab1cbebead6"

TWILIO_SID = account_sid
TWILIO_AUTH_TOKEN = auth_token
TWILIO_VIRTUAL_NUMBER = "+14235566393"
TWILIO_VERIFIED_NUMBER = "+91 9050763281"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)



