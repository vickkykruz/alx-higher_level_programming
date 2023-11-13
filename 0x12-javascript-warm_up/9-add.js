#!/usr/bin/node

/* Write a script that prints the addition of 2 integers */

const args = process.argv.slice(2);

const firstArg = parseInt(args[0]);
const secondArg = parseInt(args[1]);

function add (a, b) { console.log(a + b); }

add(firstArg, secondArg);
