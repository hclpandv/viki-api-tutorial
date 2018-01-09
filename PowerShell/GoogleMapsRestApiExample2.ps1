$TargetCity = Read-Host "Please Enter the City Name "


$base_Uri = "http://maps.googleapis.com/maps/api/geocode/json"
$Rest_Uri =  $($base_Uri +"?address=" + $TargetCity)

$Rest_Uri

$api_response = Invoke-RestMethod -Uri $Rest_Uri -Method Get

$address_components = $api_response.results.address_components
$lat = $api_response.results.geometry.location.lat
$lng = $api_response.results.geometry.location.lng

$address_components
$lat
$lng
