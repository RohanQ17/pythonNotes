
import smtplib
import email
import email.utils



sender = "autorelay17@gmail.com"
receiver = "axelb4467@gmail.com"
password ="wusyaotlmlxhtfuj"
subject = "email automation by python"
body= "heres your email "

message= f"""From: Rohan Tomar {sender}
To: snoop dogg {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender,password)
print("loggin in")

server.sendmail(sender, receiver, message)
print("email has been sent")
