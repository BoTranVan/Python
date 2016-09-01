var formidable = require("formidable");
	http = require("http");
	util = require("util");


http.createServer(function (request, response) {
	if (request.url === "/upload" && request.method.toLowerCase() === "post") {
		var form = new formidable.IncomingForm();
		form.parse(request, function (errors, fields, files) {
			response.writeHead(200, {"Conten-Type": "text/plain"});
			response.write("Received upload. \n\n");
			response.end(util.inspect({fields: fields, files: files}));
		});
		return;
	}
	response.writeHead(200, {"Content-Type": "text/html"});
	response.end(
		'<form action="/upload" enctype="multipart/form-data" '+
		'method="post">'+
		'<input type="text" name="title"><br>'+
		'<input type="file" name="upload" multiple="multiple"><br>'+
		'<input type="submit" value="Upload">'+
		'</form>'
	);
}).listen(8888);