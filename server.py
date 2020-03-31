from flask import Flask, render_template
import json
w = json.load(open('worldl.json'))
app = Flask(__name__)
@app.route('/country/<i>')
def country(i):
	return render_template('country.html', c = w[int(i)])


@app.route('/')
def index():
	return "Information about <a href=country/42>Cuba</a>."

if __name__== '__main__':
	app.run(debug=True)