#!/usr/bin/node

/* Write a script that prints a square */

const args = process.argv.slice(2);

if (!parseInt(args[0])) console.log('Missing size');
else {
  for (let i = 0; i < parseInt(args[0]); i++) console.log('X'.repeat(args[0]));
}
