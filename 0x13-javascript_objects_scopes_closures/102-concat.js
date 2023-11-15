#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const fileA = args[2];
const fileB = args[3];
const fileC = args[4];

if (fileA && fileB && fileC) {
  fs.open(fileA, 'r', () => {

  });
}
