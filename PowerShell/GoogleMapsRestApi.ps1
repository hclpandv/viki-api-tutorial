<# Working PS Api Hook Code


$api_response = Invoke-RestMethod -Method Get -uri "http://maps.googleapis.com/maps/api/geocode/json?address=Chicago"

$lat = $api_response.results.geometry.location.lat
$lng = $api_response.results.geometry.location.lng

$lat
$lng

#>



$api_response = Invoke-WebRequest -Uri "http://maps.googleapis.com/maps/api/geocode/json?address=Chicago"

$address_components = $api_response.results.address_components
$lat = $api_response.results.geometry.location.lat
$lng = $api_response.results.geometry.location.lng


$address_components
$lat
$lng



