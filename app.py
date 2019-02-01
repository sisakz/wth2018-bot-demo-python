from flask import Flask, request, jsonify, send_from_directory
import json
import os
import requests

# Global states for store voting
yes = 0
no = 0

# Create Flask HTTP server
app = Flask(__name__)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
# Serve static webpage from /static
@app.route("/")
def index():  
	return app.send_static_file('index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_static_dir(path):
	return send_from_directory(static_file_dir, path)

# /api/vote endpoint
# GET - get vote result
# POST - submit a new vote
@app.route("/api/vote", methods = ['POST', 'GET'])
def vote():
		global yes, no
		if request.method == 'GET':
				return jsonify(yes = yes, no = no)
		if request.method == 'POST':
				vote = request.json["vote"]
				if vote == "yes":
					yes += 1
				else:
					no += 1	
				return jsonify(yes = yes, no = no)

# /api/hook endpoint
# POST - webhook for the bot
@app.route("/api/hook", methods = ['POST', 'GET'])
def hook():
	global webhookMessage
	if request.method == 'GET':
		return webhookMessage
	if request.method == 'POST':
		webhookMessage = request.json
		messageId = webhookMessage["data"]["id"]
		message = getMessage(messageId)
		print(message)
		processMessage(message)
		return jsonify(webhookMessage)

# GET message by messageId
def getMessage(messageId):
	url = "https://api.ciscospark.com/v1/messages/" + messageId
	r = requests.get(url, headers={'Authorization': 'Bearer MDUwMjExYjAtYjVmZS00MWFiLWFjN2QtMzQ3ZmY1YWYxNDFmMmFkMTJmMTctM2Jm_PF84_4a05e5c1-65cb-4f86-899f-dbcc12a1af24'})
	return r.json()["text"]

def processMessage(message):
	botname = messages[17:] #- 2== "wth2018-vote-demo"
	print botname

# run the app
if __name__ == "__main__":
	# run Flask HTTP server
	app.run()