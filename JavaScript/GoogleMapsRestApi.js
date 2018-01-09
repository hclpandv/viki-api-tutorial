
function initialize()
{
    var myLatLng = new google.maps.LatLng(28.617161,77.208111);
    var map = new google.maps.Map(document.getElementById("map"),
    {
        zoom: 17,
        center: myLatLng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var marker = new google.maps.Marker(
    {
        position: myLatLng,
        map: map,
        title: 'Rajya Sabha'
    });
}