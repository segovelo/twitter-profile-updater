from email.message import EmailMessage
from re import sub
import ssl
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")

class Email():
    def __init__(self):
        pass

    def send(self, json = None):
        subject = 'Nasa Content api.nasa.gov/planetary/apod'
        body = """
        This is a test email, send from python script to automate the process.
        
        title : {}
        explanation : {}
        imageURL : {}
        imageHDURL : {}
        media_type : {}
        date : {}
        """.format(json['title'],json['explanation'],json['url'],json['hdurl'],json['media_type'],json['date'])

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
            smpt.login(email_sender, email_password)
            smpt.sendmail(email_sender, email_receiver, em.as_string())
