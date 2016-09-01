var fs = require("fs");

// var data = fs.readFileSync("plainText.txt");

// console.log(data.toString());

fs.readFile("plainText.txt", function(error, data){
	if (error) return console.error(error);
	console.log(data.toString())
});

console.log('Ended.')