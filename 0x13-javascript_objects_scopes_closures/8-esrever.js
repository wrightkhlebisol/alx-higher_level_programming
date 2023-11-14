#!/usr/bin/node

function esrever (list) {
  let p1 = 0;
  let p2 = list.length - 1;

  while (p1 < p2) {
    // Swap
    const temp = list[p1];
    list[p1] = list[p2];
    list[p2] = temp;

    p1++;
    p2--;
  }
  return list;
}

module.exports = { esrever };
