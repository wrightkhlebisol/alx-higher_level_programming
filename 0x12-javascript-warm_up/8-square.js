#!/usr/bin/node
const numP = parseInt(process.argv[2]);

if (!numP) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < numP) {
    console.log('X');
    i++;
  }
}
