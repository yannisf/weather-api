var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: new google.maps.LatLng(38.2, 24),
    mapTypeId: google.maps.MapTypeId.TERRAIN
});

var infowindow = new google.maps.InfoWindow();

var marker, i;

for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        title: locations[i][0],
        map: map
    });

    google.maps.event.addListener(marker, 'click', (function (marker, i) {
        return function () {
            infowindow.setContent('<a href="http://api.openweathermap.org/data/2.5/weather?id=' +
                locations[i][3] +
                '&appid=58774c7e6436905dbf5aa6af105e943c&units=metric&mode=html">' +
                locations[i][0] + '</a>');
            infowindow.open(map, marker);
        }
    })(marker, i));
}
