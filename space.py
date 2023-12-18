# Import packages
import urllib.request
import json

def space():
	# Uses OpenNotify API to construct a message
	url = "http://api.open-notify.org/astros.json"
	request = urllib.request.urlopen(url)
	result = json.loads(request.read())

	# Returns the space message in from of a string
	return f"Space Fact:\nThere are {result['number']} people in space."