#!/usr/bin/node
const numP = parseInt(process.argv[2]);

if (!numP) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  let lineFeed = '';
  while (i < numP) {
    while (j < numP) {
      lineFeed += 'X';
      j++;
    }
    console.log(lineFeed);
    i++;
  }
}
