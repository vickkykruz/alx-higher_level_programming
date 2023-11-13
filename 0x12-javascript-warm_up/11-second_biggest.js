#!/usr/bin/node

/* Write a script that searches the second biggest integer in the list of
 * arguments.
 */

const args = process.argv.slice(2);

if (args.length < 2) console.log(0);
else {
  for (let i = 0; i < args.length; i++) args[i] = Number(args[i]);

  let bigNum;
  let secBigNum;

  if (args[0] >= args[1]) {
    bigNum = args[0];
    secBigNum = args[1];
  } else {
    bigNum = args[1];
    secBigNum = args[0];
  }

  for (let i = 2; i < args.length; i++) {
    if (args[i] > bigNum) {
      secBigNum = bigNum;
      bigNum = args[i];
    } else if (args[i] > secBigNum && args[i] < bigNum) {
      secBigNum = args[i];
    }
  }

  console.log(secBigNum);
}
