#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const testStr = '18';
let count = 0;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    JSON.parse(body).results.forEach(result => {
      result.characters.forEach(character => {
        const charArray = character.split('/');
        if (charArray.includes(testStr)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
