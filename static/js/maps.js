function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        center: {
            lat: 51.509865,
            lng: -0.118092
        }
    });

    // Create an array of alphabetical characters used to label the markers.
    const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    //Create London's longtitude and latitude for location maps
    var locations = [
          { lat: 51.507465, lng: 0.127809 },
          { lat: 51.483465, lng: 0.058692 },
    ];

    const markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    // Add a marker clusterer to manage the markers.
    
    var markerCluster = new MarkerClusterer(map, markers, 
    { imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer/m" });

}