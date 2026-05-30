from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

template = Template(Path(r'C:\Repos\PythonProjects\completePythonMastery\template.html').read_text())


message = MIMEMultipart()
message['From'] = 'Thomas Johnson'
message['To'] = "testuser@codewithmosh.com"
message['Subject'] = 'This is a test email'
body = template.substitute(name='Thomas')
message.attach(MIMEText(body, 'html'))
message.attach(MIMEImage(Path(r'C:\Repos\PythonProjects\completePythonMastery\9-PythonStandardLibrary\TBear_Waving.jpg').read_bytes()))


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #Identify ourselves to the email server
    smtp.starttls() #Encrypt the connection
    smtp.login('ketesteralpha@gmailcom', 'L3tInTh3Dud3m@n') #Login to the email server
    smtp.send_message(message) #Send the email
    print('Email sent successfully')
