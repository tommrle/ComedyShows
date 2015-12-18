var express = require('express');
var app = express();
var fs = require('fs');
var obj;
fs.readFile(__dirname + "/../data/current/current.json", 'utf8', function(err, data) {
	if (err) throw err;
	obj = JSON.parse(data);
	console.log("Data ready");
});


const PORT = 8080;

app.get('/', function(req, res) {
	res.send('Hello World!');
});

app.get('/allshows/', function(req, res) {
	res.send(obj);
});

app.get('/img/:image_url', function(req, res) {
	console.log('Image Requested: ' + req.params.image_url);
	fs.readFile(__dirname + "/../img/" + req.params.image_url, function(err, data) {
		if (err) {
			console.log('Cannot find: ' + req.params.image_url);
			console.log('Error: ' + err);
		} else {
			console.log('Serving: ' + req.params.image_url);
			res.writeHead(200, {'Content-Type':'image/jpeg'});
			res.end(data);
		}
	});
});

var server = app.listen(PORT, function() {
	var host = server.address().address;
	var port_num = server.address().port;
	console.log('Server is listening at http://%s:%s', host, port_num);
});