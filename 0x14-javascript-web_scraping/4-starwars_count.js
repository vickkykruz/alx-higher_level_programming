#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const results = JSON.parse(body).results;
  let count = 0;
  for (const result of results) {
    result.characters.forEach(character => {
      if (character.includes('18')) count++;
    });
  }
  console.log(count);
});
