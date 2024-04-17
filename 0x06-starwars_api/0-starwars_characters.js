#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const rootURL = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';
// console.log(rootURL);
request(rootURL, (error, response, body) => {
  if (error) throw new Error(error);

  const parseBody = JSON.parse(body);
  for (const charsLink of parseBody.characters) {
    request(charsLink, (error, rsponse, body) => {
      if (error) throw new Error(error);
      const parsedCharacter = JSON.parse(body);
      console.log(parsedCharacter.name);
    });
  }
});
