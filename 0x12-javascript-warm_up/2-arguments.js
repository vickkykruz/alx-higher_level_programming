#!/usr/bin/node

/* Write a script that prints a message depending of the number of arguments
 * passed:
 */

const args = process.argv.slice(2);

if (!args.lenght) console.log('No argument');
else if (args.lenght === 1) console.log('Argument found');
else console.log('Arguments found');
