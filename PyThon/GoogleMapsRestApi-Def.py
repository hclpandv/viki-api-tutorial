import urllib, json, time
def GoogGeoAPI(address,api="",delay=5):
  base = "https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + address.replace(" ","+")
  GeoUrl = base + addP # + "&key=" + api
  response = urllib.urlopen(GeoUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    finList = [resu['formatted_address'],resu['geometry']['location']['lat'],resu['geometry']['location']['lng']]
  else:
    finList = [None,None,None]
  time.sleep(delay) #in seconds
  return finList
  

 
print(GoogGeoAPI("Delhi"))