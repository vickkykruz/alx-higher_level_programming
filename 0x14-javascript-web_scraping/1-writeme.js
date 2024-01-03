#!/usr/bin/node
const request = require('fs');
request.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  if (error) console.log(error);
});
