#!/usr/bin/node

/* Write a script that prints x times “C is fun” */

const args = process.argv.slice(2);

if (!parseInt(args)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < parseInt(args); i++) console.log('C is fun');
}
