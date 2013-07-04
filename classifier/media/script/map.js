// Google Maps realisation

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

// Rainbow colors
var color_rainbow = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "0000FF",
                     "#4B0082", "#8B00FF"];
var color_bootstrap = ["#999999", "#468847", "#f89406", "#b94a48", "#3a87ad",
                       "#333333"]

var markersArray = [];

function getColor() {
   return color_bootstrap[Math.floor(Math.random() * color_bootstrap.length)];
}

function initialize() {
    var myLatLng = new google.maps.LatLng(0, 0);
    var myOptions = {
        center: myLatLng,
        zoom: 2,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);

    var twitt_count = 10;

    var message_count = 0;
    function showTwitt(response) {
        $('.twitts').after(function() {
            var twitt = response;
            if (message_count >= twitt_count) {
                $('.twitt')[twitt_count - 1].remove();
                message_count -= 1;
            }
            if (twitt.text.length > 19)
                return '<div class="twitt" style="display: none">' + twitt.text.substr(0, 19) + '...</div>';
            var message = '<div class="twitt" style="display: none">' + twitt.text + '</div>';
            return message;
        });
        $('.twitt').show('slow');
        message_count += 1;
    }

    var marker_count = 0;
    function responseCallback(response) {
        var n = 0;
        while (n < response.length) {
            var twitt = response[n];
            var myLatLng = new google.maps.LatLng(twitt.coordinates[1],
                                                  twitt.coordinates[0]);
            if (twitt.text.length > 19)
                twitt.text = twitt.text.substr(0, 25) + '...';
            if (marker_count >= twitt_count) {
                markersArray[0].setMap(null);
                markersArray.splice(0, 1);
                marker_count -= 1;
            }
            markersArray.push(new StyledMarker({
                styleIcon: new StyledIcon(StyledIconTypes.BUBBLE,
                    {color: getColor(), text: twitt.text}),
                    position: myLatLng,
                    map: map
                })
            );
            marker_count += 1;
            n++;
        }
    }

    var id = '0';
    function getTwitts() {
        $.ajax({
            type: "GET",
            data: { "id": id },
            url: "/get_messages/",
            success: function(response) {
                var n = 0;
                while (n < response.length) {
                    id = response[n].id;
                    showTwitt(response[n]);
                    n++;
                }
                responseCallback(response);
                getTwitts();
            }
        });
    }

    getTwitts();
}

google.maps.event.addDomListener(window, "load", initialize);