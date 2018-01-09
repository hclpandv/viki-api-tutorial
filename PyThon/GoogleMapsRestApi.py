import urllib, json, time
base = "https://maps.googleapis.com/maps/api/geocode/json?"
addP = "address=" + "Delhi"
GeoUrl = base + addP
response = urllib.urlopen(GeoUrl)
jsonRaw = response.read()
print(jsonRaw) #For Testing

