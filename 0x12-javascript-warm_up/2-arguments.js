#!/usr/bin/node
const argLen = process.argv.length;
if (argLen <= 2) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
