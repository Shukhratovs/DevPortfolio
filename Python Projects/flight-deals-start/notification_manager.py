from twilio.rest import Client
import smtplib

TWILIO_SID = 'ACe77b3844ac224451a746506b3d02d2c3'
TWILIO_AUTH_TOKEN = '52c3d99995d10ee94b791192bae586d1'
TWILIO_VIRTUAL_NUMBER = '+18556052350'
TWILIO_VERIFIED_NUMBER = '+15204359192'

MY_EMAIL = "khumoyunshukhratov@gmail.com"
MY_PASSWORD = "ywls djot phvi clgd"

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

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )

