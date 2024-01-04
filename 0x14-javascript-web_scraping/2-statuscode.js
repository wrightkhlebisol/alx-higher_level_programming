#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${res.statusCode}`);
});
