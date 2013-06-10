import urllib, urllib2
try:
    import json
except ImportError:
    import simplejson as json

params = {'address': '5903 Laurium Rd, Charlotte, NC', 'sensor': 'false'}
url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

rawreply = urllib2.urlopen(url).read()
reply = json.loads(rawreply)
print reply['results'][0]['geometry']['location']
