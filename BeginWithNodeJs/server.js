var http = require("http");
var url = require("url");

function start (route, handle) {
	 function onRequest(request, response) {
	 	var postData = "";
	 	var pathname = url.parse(request.url).pathname;
	  	console.log("Resquest for " + pathname +" received.");

	  	// route(pathname);
	  	request.setEncoding("utf8");

	  	request.addListener("data", function (postDataChunk) {
	  		postData = postData + postDataChunk;
	  		console.log("Received POST data chunk: " + postDataChunk);
	  	});
	  	// response.writeHead(200, {"Content-Type": "text/plain"});
	  	request.addListener("end", function () {
		  	route(handle, pathname, response, postData);
	  	});

	  	// response.write("Hello World.");
	  	// response.end();
	  }

	http.createServer(onRequest).listen(80);
	console.log("Server running at http://Anonymous")
}

exports.start = start;