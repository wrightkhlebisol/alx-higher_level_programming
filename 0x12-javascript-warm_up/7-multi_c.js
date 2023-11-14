#!/usr/bin/node
const numP = parseInt(process.argv[2]);

if (!numP) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < numP) {
    console.log('C is fun');
    i++;
  }
}
