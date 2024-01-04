#!/usr/bin/node
const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      return resolve(body);
    });
  });
}

async function queryById () {
  const body = await requestPromise(url);
  const characterURL = JSON.parse(body).characters;
  const charResponse = characterURL.map(async url => await requestPromise(url));
  const characterDetails = await Promise.all(charResponse);
  characterDetails.forEach((characterDetail) => console.log(JSON.parse(characterDetail).name));
}

queryById();
/**
request(url, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  JSON.parse(body).characters.forEach(characterURL => {
    request(characterURL, (err, res, body) => {
      if (err) {
        return console.error(err);
      }
      setTimeout(() => console.log(JSON.parse(body).name), 1000);
    });
  });
});
*/
