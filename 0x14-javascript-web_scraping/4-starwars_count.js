#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const testStr = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  JSON.parse(body).results.forEach(result => {
    if (result.characters.includes(testStr)) {
      count++;
    }
  });
  console.log(count);
});
