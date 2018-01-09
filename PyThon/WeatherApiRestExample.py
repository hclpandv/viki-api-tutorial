import json, requests, sys, urllib
print '\n'
location = raw_input("Please Enter a valid City..")
print '\n'
base_uri = "http://api.openweathermap.org/data/2.5/weather?q=%s" % (location)
key = 'f1a52e0d2011b0b4f042744e05ce2498'
url = base_uri + '&APPID=' + key
api_response = urllib.urlopen(url)
jsonRaw = api_response.read()
diction = json.loads(jsonRaw)
city = diction["name"]
print("City name you selected is : " + city)
print '\n'
print ('*******Coordinates of %s*******') %(location)
lat=diction["coord"]["lat"]
lon=diction["coord"]["lon"]
print("Latitude is .....")
print(lat)
print("Longitude is .....")
print(lon)
print '\n'
print ('*******TEMPERATURE DETAILS*******')
ctemp = float(diction["main"]["temp"])
print ("Current temperature is .....")
print (ctemp, 'In Kelvin')
tempmax = float(diction["main"]["temp_max"])
print ("Max temperature is .....")
print (tempmax, 'In Kelvin')
tempmin = float(diction["main"]["temp_min"])
print ("Min temperature is .....")
print (tempmin, 'In Kelvin')
print '\n' 
