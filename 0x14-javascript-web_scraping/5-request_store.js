#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
request(args[0]).pipe(fs.createWriteStream(args[1]));
