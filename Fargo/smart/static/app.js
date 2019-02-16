$(function () {
	socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.on ('connect', function() {
		$('.redled').attr('class','redled');
		$('.greenled').attr('class','greenled active');
    	socket.emit('client_connected', {'data': 'New client!'});
	});

	socket.on ('disconnect', function() {
		$('.redled').attr('class','redled active');
		$('.greenled').attr('class','greenled');
	});

	socket.on ('alert', function (data) {
        $('#RedAlert').attr("hidden", data);
        if (!data) {
			$('.CodeZone').attr("hidden", false);
		}
	});

	$("#SendCode").click(function () {
        let code = $("#TypeCode").val();
	   	socket.emit('auth', {'data': code});
		$('.CodeZone').attr("hidden", true);
	});

	socket.on ('temperature', function (data) {
        $('#tc').html(data.toString() + " °C");
	});

	socket.on ('lumen', function (data) {
		$('#lux').html(data.toString());
		let bright = Math.max(1 - data/250, 0) * 100;
		$('.light-ring').css({
			"background-color": "#ffff00",
			"filter": "brightness(" + bright + "%)"
		});
	});
});