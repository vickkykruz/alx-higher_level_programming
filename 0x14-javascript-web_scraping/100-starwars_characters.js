#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    for (const character of characters) {
      /* console.log(character); */
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          const characterName = JSON.parse(body);
          console.log(characterName.name);
        } else {
          console.log(`code: ${response.statusCode}`);
        }
      });
    }
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
