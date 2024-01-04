#!/usr/bin/node
const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  JSON.parse(body).characters.forEach(characterURL => {
    request(characterURL, (err, res, body) => {
      if (err) {
        return console.error(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
