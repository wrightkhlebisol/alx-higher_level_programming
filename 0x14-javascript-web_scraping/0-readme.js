#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const fileName = process.argv[2];
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
