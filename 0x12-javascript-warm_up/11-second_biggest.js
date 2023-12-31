#!/usr/bin/node
const pArgs = process.argv;

if (!pArgs[2]) {
  console.log(0);
} else if (pArgs.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  let firstHighest = parseInt(pArgs[2]);
  let secondHighest = parseInt(pArgs[2]);

  while (i < pArgs.length) {
    const currArg = parseInt(pArgs[i]);
    if (currArg > firstHighest && currArg > secondHighest) {
      secondHighest = firstHighest;
      firstHighest = currArg;
    } else if (currArg > secondHighest && currArg < firstHighest) {
      secondHighest = currArg;
    }
    i++;
  }
  console.log(secondHighest);
}
