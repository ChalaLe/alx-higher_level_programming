#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const numArgs = args.length;

if (numArgs === 0) {
  console.log(0);
} else if (numArgs === 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < numArgs; i++) {
    const num = args[i];
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
