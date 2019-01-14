from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('curbstonecoder@gmail.com', 'May.16.1996')

app = Flask(__name__)

def send_details(request):
	info = MIMEMultipart()
	info['From'] = 'curbstonecoder@gmail.com'
	info['To'] = 'tristanpowers74@gmail.com'
	info['Subject'] = 'New Message'
	name = request.form['name']
	number = request.form['number']
	details = request.form['details']
	text = "Name: " + name + "\n" + "Number: " + number + "\n" + "Details: " + details + "\n"
	body = MIMEText(text, "plain")
	info.attach(body)
	s.sendmail("curbstonecoder@gmail.com", "tristanpowers74@gmail.com", info.as_string())

@app.route('/', methods=['POST'])
def get_message():
	if request.method == 'POST':
		send_details(request)
		return render_template('index.html')

@app.route('/')
def start_page():
	return render_template('index.html')

@app.route('/message', methods=['POST'])
@app.route('/message')
def message_page():
	return render_template('message_page.html')

@app.route('/contact')
def contact_page():
	return render_template('contact_page.html')

@app.route('/static_websites')
def static_websites():
	return render_template('static_websites.html')

@app.route('/dynamic_websites')
def dynamic_websites():
	return render_template('dynamic_websites.html')

@app.route('/responsive_display')
def responsive_display():
	return render_template('responsive_display.html')

@app.route('/maintenance')
def maintenance():
	return render_template('maintenance.html')

if __name__ == '__main__':
	app.run(debug = True)
