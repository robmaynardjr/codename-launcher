var express = require('express');
var app = express();

app.all("/", function (req, res){
    app.use(express.static(__dirname + '/public/'));
    res.sendFile(__dirname + '/public/index.html');
    console.log(req.ip);
});

app.listen(8080);