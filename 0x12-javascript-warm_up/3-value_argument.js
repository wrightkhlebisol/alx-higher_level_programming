#!/usr/bin/node
const arg2 = process.argv[2];
if (!arg2) {
  console.log('No argument');
} else {
  console.log(arg2);
}
