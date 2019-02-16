function lighter(cible, onoff) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","http://192.168.2.14:5000/led/" + onoff + (cible == '' ? '' : '/') + cible, false);
    xmlHttp.send(null);
    console.log("http://192.168.2.14:5000/led/" + onoff + (cible == '' ? '' : '/') + cible);
    return xmlHttp.responseText;
}

document.getElementById('switch-all').onclick = function() {
    if ( this.checked ) {
        console.log("All leds on");
        lighter('', 'on');
    } else {
        console.log("All leds off");
        lighter('', 'off');
    }
};

document.getElementById('switch-led1').onclick = function() {
    if ( this.checked ) {
        console.log("Led1 on");
        lighter(18, 'on');
    } else {
        console.log("Led1 off");
        lighter(18, 'off');
    }
};

document.getElementById('switch-led2').onclick = function() {
    if ( this.checked ) {
        console.log("Led2 on");
        lighter(24, 'on');
    } else {
        console.log("Led2 off");
        lighter(24, 'off');
    }
};
