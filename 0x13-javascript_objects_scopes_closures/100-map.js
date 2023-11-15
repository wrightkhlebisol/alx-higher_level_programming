#!/usr/bin/node
const { list } = require('./100-data.js');

console.log(list);
const nList = list.map((l, i) => l * i);
console.log(nList);
