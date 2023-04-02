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
    const locations = [
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
    
    const markerCluster = new MarkerClusterer(map, markers, 
    { imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer/m" });
}

// Back to top button

// Create toggle
window.onscroll = () => {
    toggleTopButton();
}

// When user clicks on the button, scroll to the top of the page with scroll behavior of smooth.
function scrollToTop(){
    window.scrollTo({top: 0, behavior: 'smooth'});
}
  
// When user scrolls down 20px from the top of the page, display button
function toggleTopButton() {
    if (document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20) {
      document.getElementById('back-to-up').classList.remove('d-none');
    } else {
      document.getElementById('back-to-up').classList.add('d-none');
    }
}