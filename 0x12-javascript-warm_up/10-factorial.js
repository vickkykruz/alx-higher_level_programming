#!/usr/bin/node

/* Write a script that computes and prints a factorial */

const args = process.argv.slice(2);
const num = parseInt(args[0]);

function factorial (n) {
  if (!n) return 1;
  else return n * factorial(n - 1);
}

console.log(factorial(num));
