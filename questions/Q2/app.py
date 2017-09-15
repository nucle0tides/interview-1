from flask import Flask, render_template, jsonify, abort, redirect, url_for
import datetime
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def index(): 
	return redirect(url_for('comments', id=100))

@app.route('/engagement/comments/<id>/', methods=['GET'])
def comments(id): 
	BASE_URL = 'https://mysidewalk.com/api/engagement/v1/comments/'
	try: 
		response = urllib.request.urlopen("{}{}{}".format(BASE_URL, id, '.json'))
		data = json.loads(response.read().decode())
		return render_template('/engagement/comments/index.html', response = comment_formatter(data)), 200
	except urllib.error.HTTPError as e:
		abort(404)

def comment_formatter(response): 
	return { 
		'comment' : response['comments'][0]['text'],
		'author_name' : "{} {}".format(response['linked']['users'][0]['firstName'], response['linked']['users'][0]['lastName']),
		'author_portrait' : response['linked']['media'][0]['url'],
		'author_bio' : response['linked']['users'][0]['bio'],
		'created' : datetime.datetime.strptime(response['comments'][0]['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%m/%d/%Y %H:%M:%S'),
		'modified' : datetime.datetime.strptime(response['comments'][0]['modifiedAt'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%m/%d/%Y %H:%M:%S'),
	}

if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)