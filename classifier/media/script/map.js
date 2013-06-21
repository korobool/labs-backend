// Google Maps realisation

// Approximately Kiev position
var latitude = 50;
var longitude = 30;
// Rainbow colors
var color = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "0000FF", "#4B0082", "#8B00FF"];

var markersArray = [];

function getColor() {
   return color[Math.floor(Math.random() * color.length)];
}

// function initialize() {
//    var LatLng = new google.maps.LatLng(latitude, longitude);
//    var map_canvas = document.getElementById('map-canvas');
//    var map_options = {
//        center: LatLng,
//        zoom: 5,
//        mapTypeId: google.maps.MapTypeId.ROADMAP
//    };
//    var map = new google.maps.Map(map_canvas, map_options);
//    marker = new google.maps.Marker({
//        animation: google.maps.Animation.DROP,
//        draggable: true,
//        map: map,
//        position: LatLng,
//    });
//    // google.maps.event.addListener(marker, 'click', toggleBounce);
//    // google.maps.event.addListener(marker, 'mouseup', changePosition);
// }
// function toggleBounce() {
//        if (marker.getAnimation() != null) {
//        marker.setAnimation(null);
//        } else {
//        marker.setAnimation(google.maps.Animation.BOUNCE);
//        }
// }
// function changePosition() {
//        var latitude = marker.getPosition().jb;
//        var longitude = marker.getPosition().kb;
//        $('#latitude').val(latitude);
//        $('#longitude').val(longitude);
// }

function initialize() {
    var myLatLng = new google.maps.LatLng(0, 0);
    var myOptions = {
        center: myLatLng,
        zoom: 1,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);

    // Main google map loop
    // window.setInterval(function() {
    //     var styleMaker3 = new StyledMarker({
    //         styleIcon: new StyledIcon(StyledIconTypes.BUBBLE,{color: "0000ff", text: "I love this label!"}),
    //         position: new google.maps.LatLng(37.263477473067, -121.880502070713),
    //         map:map
    //         });
    //     }, 5000);

    // var i = 0;
    // function setMarker () {
    //      setTimeout(function () {
    //      var beach = beaches[i];
    //      var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
    //      var styleMaker = new StyledMarker({
    //              styleIcon: new StyledIcon(StyledIconTypes.BUBBLE,{color: "00ff00", text: beach[0]}),
    //              position: myLatLng,
    //              map: map
    //      });
    //      i++;
    //      if (i < beaches.length) {
    //          setMarker();
    //      }
    //      }, 3000)
    // }
    // setMarker();

    var twitt_counter = 0;
    function showTwitt(response) {
        var twitt = $('.twitts').after(function() {
            var twitt = JSON.parse(response);
            if (twitt_counter >= 10) {
                $('.twitt')[0].remove();
            }
            return '<div class="twitt">' + twitt.text + '</div>';
        });
        twitt_counter += 1;
    }

    var marker_counter = 0;
    function responseCallback(response) {
        var n = 0;
        while (n < response.length) {
            var twitt = JSON.parse(response[n]);
            var myLatLng = new google.maps.LatLng(twitt.coordinates[1],
                                                  twitt.coordinates[0]);
            if (marker_counter >= 10) {
                // $('.twitt')[0].remove();
                markersArray[0].setMap(null);
                markersArray.splice(0, 1);
                // delete markersArray[0];
            }
            markersArray.push(new StyledMarker({
                styleIcon: new StyledIcon(StyledIconTypes.BUBBLE,
                    {color: getColor(), text: twitt.text}),
                    position: myLatLng,
                    map: map
                })
            );
            marker_counter += 1;
            n++;
        }
        getTwitts();
    }

    function getTwitts() {
        $.ajax({
            type: "get",
            url: "/get_messages/",
            success: function(response) {
                responseCallback(response);
                showTwitt(response);
            }
        });
    }

    getTwitts();    
}

google.maps.event.addDomListener(window, "load", initialize);