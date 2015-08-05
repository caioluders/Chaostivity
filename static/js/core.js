function draw( d , o ) {
	var c = document.getElementById("pareidolia");
	var ctx = c.getContext("2d");
	ctx.clearRect(0, 0, c.width, c.height);
	ctx.save()
	ctx.globalAlpha = parseInt(o)/100
	
	var ss = document.styleSheets;
    for (var i = 0, max = ss.length; i < max; i++) {
        if (ss[i].href == "static/styles/print_style.css") {
        	console.log("wtf") ;
            c.width = 2480;
        	c.height = 3508;
        }
    }

	for (var i = 0 ; i < parseInt(d) ; i++ ) {
		ctx.beginPath();
		ctx.moveTo( Math.floor((Math.random() * c.width)) ,Math.floor((Math.random() * c.height)));
		ctx.lineTo(Math.floor((Math.random() * c.width)),Math.floor((Math.random() * c.height)));
		ctx.lineWidth = 0.5;
		ctx.globalAlpha = parseInt(o)/100
		ctx.stroke();
	}

	for (var i = 0 ; i < parseInt(d) ; i++ ) {
		ctx.beginPath();
		ctx.moveTo( Math.floor((Math.random() * c.width)) ,Math.floor((Math.random() * c.height)));
		ctx.bezierCurveTo(Math.floor((Math.random() * c.width)), Math.floor((Math.random() * c.height)), Math.floor((Math.random() * c.width)), Math.floor((Math.random() * c.height)), Math.floor((Math.random() * c.width)), Math.floor((Math.random() * c.height)));
		ctx.lineWidth = 0.5;
		ctx.globalAlpha = parseInt(o)/100
		ctx.stroke();
	}

	ctx.restore()
}

function downloadCanvas(link, canvasId, filename) {
    link.href = document.getElementById(canvasId).toDataURL();
    link.download = filename;
}

// document.getElementById('download_out').addEventListener('click', function() {
//     downloadCanvas(this, 'pareidolia', 'pareidolia.png');
// }, false);

function wtf() {
	alert("I don't know WTF IS THIS !");
}

function select_print(t) {
	console.log(t) ;
}

var canvas = document.getElementById("title_background");
var c = canvas.getContext("2d");

c.fillStyle = 'rgb(114,152,63)';
// c.roundRect(0, 0, 230, 80, {lowerLeft:10,lowerRight:10 , upperLeft:10 , upperRight:10}, true, false);
c.beginPath() ;
c.moveTo(10,0) ;
c.lineTo(220,0) ;
c.quadraticCurveTo(230 , 0 , 230 , 10 );
c.lineTo(230,70) ;
c.quadraticCurveTo(230 , 80 , 220 , 80 );
c.lineTo(10,70) ;
c.quadraticCurveTo(0 , 70 , 0 , 60 );
c.lineTo(0,10) ;
c.quadraticCurveTo(0 , 0 , 10 , 0 );
c.closePath() ;
c.fill() ;

c.fillStyle = "white";
c.shadowOffsetX = -3 ;
c.shadowOffsetY = 3 ;
c.shadowBlur = 0 ;
c.shadowColor = 'rgb(87,115,49)' ;
c.font = "35px Conv_Anothershabby_trial";
c.fillText("Chaostivity", 25, 50);

draw(50) ;