#!/usr/bin/env node
const fs = require('fs');
const process = require('process');

const fileName = process.argv[2];
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
