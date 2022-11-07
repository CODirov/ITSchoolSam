import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = "itschoolsam@gmail.com"
    password = "dtebvycgcofzhmek"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "IT school Samarkand"
        server.sendmail(sender, sender, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def send_msg(msg):
    send_email(message=msg)
