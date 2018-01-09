import urllib, json, time
base_uri = "https://maps.googleapis.com/maps/api/geocode/json?"
addP = "address=" + "Delhi"
rest_uri = base_uri + addP
api_response = urllib.urlopen(rest_uri)
jsonRaw = api_response.read()
print(jsonRaw) #For Testing

jsonData = json.loads(jsonRaw)

print(jsonData)

