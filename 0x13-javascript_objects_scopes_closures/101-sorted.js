#!/usr/bin/node

const { dict } = require('./101-data.js');
const nDict = {};

for (const k in dict) {
  const index = dict[k];
  if (typeof nDict[index] !== 'object') {
    nDict[index] = [];
    nDict[index].push(k);
  } else {
    nDict[index].push(k);
  }
}

console.log(nDict);
