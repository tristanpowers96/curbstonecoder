import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# set up the SMTP server

def send_email(person):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login('curbstonecoder@gmail.com', 'May.16.1996')

	info = MIMEMultipart()
	info['From'] = 'curbstonecoder@gmail.com'
	info['To'] = 'tristanpowers74@gmail.com'
	info['Subject'] = 'New Message'
	name = person['Contact']['Name']
	number = person['Contact']['Number']
	email = person['Contact']['Email']
	details = person['Contact']['Details']
	method = person['Contact']['Method']
	time = person['Contact']['Time']
	text = """
	Received: {}
	Name: {}
	Number: {}
	Email: {}
	Preferred contact method: {}
	Details: {}""".format(time, name, number, email, method, details)
	body = MIMEText(text, "plain")
	info.attach(body)
	s.sendmail("curbstonecoder@gmail.com", "tristanpowers74@gmail.com", info.as_string())
