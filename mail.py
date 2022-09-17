from json_functions import json_functions
import ssl
import smtplib
from email.message import EmailMessage

class mail:
    def __init__(self) -> None:
        pass

    def send_mail(self,price,price_temporary)->None:

        body = f"""ZMIANA CEN SŁUCHAWEK
        xm4_black:{price['media_black_xm4']} => {price_temporary['media_black_xm4']}
        xm4_blue:{price['media_blue_xm4']} => {price_temporary['media_blue_xm4']}
        xm5_black:{price['media_black_xm5']} => {price_temporary['media_black_xm5']}
        xm5_white:{price['media_white_xm5']} => {price_temporary['media_white_xm5']}"""
        json_functions.save_json("price",price_temporary)

        config = json_functions().open_json("config")
        email_sender = config['sender']
        email_password = config['password']
        email_receiver = config['receiver']


        subject = 'Zmiana cen - MediaExpert'

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(body)
        pass