from flask import Flask, render_template, jsonify
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template('index.html')

@app.route('/api/engagement/v1/comments/<id>/', methods=['GET'])
def comments(id): 
	BASE_URL = 'https://mysidewalk.com/api/engagement/v1/comments/'
	response = urllib.request.urlopen("{}{}{}".format(BASE_URL, id, '.json'))
	data = json.loads(response.read().decode())
	return render_template('/engagement/comments/modal_body.html', data = data)

if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)