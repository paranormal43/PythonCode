import smtplib

MY_EMAIL = "EMAIL"
MY_PASSWORD = "EMAIL_PASSWORD"

class NotificationManager:

    def __init__(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)

    def send_email(self,message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Flight Detail\n\n{message}")

    #This class is responsible for sending notifications with the deal flight details.
    pass