#!/usr/bin/node
const request = require('fs');
request.readFile(process.argv[2], 'utf8', function (error, body) {
  console.log(error || body);
});
