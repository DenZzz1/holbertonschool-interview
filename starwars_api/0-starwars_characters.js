#!/usr/bin/node
// Script that prints all characters of a Star Wars movie, in order.
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/?format=json`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(charBody).name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
