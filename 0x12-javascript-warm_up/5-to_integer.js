#!/usr/bin/node
const arg2 = process.argv[2];
if (parseInt(arg2)) {
  console.log(`My number: ${arg2}`);
} else {
  console.log('Not a number');
}
