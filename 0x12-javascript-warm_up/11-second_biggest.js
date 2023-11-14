#!/usr/bin/node
const pArgs = process.argv;

if (!pArgs[2]) {
  console.log(0);
} else if (pArgs.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  let firstHighest = 0;
  let secondHighest = 0;

  while (i < pArgs.length) {
    if (pArgs[i] > firstHighest && pArgs[i] > secondHighest) {
      secondHighest = firstHighest;
      firstHighest = pArgs[i];
    } else if (pArgs[i] > secondHighest && pArgs[i] < firstHighest) {
      secondHighest = pArgs[i];
    }
    i++;
  }
  console.log(secondHighest);
}
