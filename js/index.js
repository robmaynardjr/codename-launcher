var express = require('express');
var app = express();

app.all("/", function (req, res){
    app.use(express.static(__dirname + '/main-gui/'));
    res.sendFile(__dirname + '/public/main-gui.html');
    console.log(req.ip);
});

app.listen(8080);