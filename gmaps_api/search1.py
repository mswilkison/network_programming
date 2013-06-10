import httplib

try:
    import json
except ImportError:
    import simplejson as json

path = ('/maps/api/geocode/json?address=5903+Laurium+Rd%2C+Charlotte%2C+NC'
	'&sensor=false')

connection = httplib.HTTPConnection('maps.googleapis.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()
reply = json.loads(rawreply)
print reply['results'][0]['geometry']['location']
