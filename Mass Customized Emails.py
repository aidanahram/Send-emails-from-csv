#Aidan Ahram
#7/11/19
#Mass Email from csv

import smtplib
import json
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#initiliaze/logins
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)

#change this based on what you want your letter to say
#rename the variables according to your usage
def compose_message(name, parameter2, parameter3, etc):
    message ="""
Hello {name},
Your{parameter2} is absolutely amazing
How is {parameter3}?
THIS IS AN EXAMPLE{etc}
    """.format(name=name, parameter2=parameter2, parameter3=parameter3, etc=etc)
    return(message)


f = open('YOUR\\FILE\\PATH.CSV', 'r' )  
# Change each fieldname to the appropriate field name. I know, so difficult.
# field name are the name of colounms 
reader = csv.DictReader( f, fieldnames = ( "name","best_food","spouse","etc", "email")) 
info = []
for row in reader:
    info.append(row)

#delete the row that is just your header
#delete this row if there are no headers in your excel
del info[0]

#Time to put it all together and shoot out emails
for item in info:
    message = MIMEMultipart("alternative")
    message['subject'] = 'YOUR SUBJECT'
    message['from'] = username 
    message['to'] = item['email']
    to = item['email']
    email_msg = compose_message(item['name'], item['best_food'], item['spouse'], item['etc'])
    email_msg = MIMEText(msg, 'text')
    message.attach(email_msg)
    server.sendmail(username, to, message.as_string())

