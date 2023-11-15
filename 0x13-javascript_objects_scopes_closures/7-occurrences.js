#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let numOccur = 0;
  let i = 0;

  while (i < list.length) {
    if (list[i] === searchElement) {
      numOccur++;
    }
    i++;
  }
  return numOccur;
}

module.exports = { nbOccurences };
