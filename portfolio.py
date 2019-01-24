from flask import Flask, render_template, request, redirect, url_for
import json
import datetime
import calendar
import send_info
app = Flask(__name__)


def send_details(request):
	name = request.form.get('name')
	number = request.form.get('number')
	email = request.form.get('email')
	preferred_method = request.form.get('contact')
	details = request.form.get('details')
	message_time = datetime.datetime.now()
	pretty_time = message_time.strftime("%A %B %d, %Y, at %I:%M %p")

	with open("contacts.json", "r") as read_file:
		file = json.load(read_file)
	person = {
		"Contact": {
			"Name": name,
			"Number": number,
			"Email": email,
			"Method": preferred_method,
			"Details": details,
			"Time": pretty_time
		}
	}
	file.append(person)
	with open("contacts.json", "w") as write_file:
		json.dump(file, write_file, indent=4, sort_keys=False)
	send_info.send_email(person)


@app.route('/', methods=['POST'])
def get_message():
	if request.method == 'POST':
		send_details(request)
		return render_template('message_received.html')

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

@app.route('/message_received', methods=['POST'])
@app.route('/message_received')
def message_received():
	return render_template('message_received.html')

if __name__ == '__main__':
	app.run(debug = True)
