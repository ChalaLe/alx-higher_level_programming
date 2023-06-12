#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  if (size <= 0) {
    console.log('Size must be a positive integer');
  } else {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
