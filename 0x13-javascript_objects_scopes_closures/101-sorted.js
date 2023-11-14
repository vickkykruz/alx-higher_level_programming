#!/usr/bin/node

/* Write a script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 */

const { dict } = require('./101-data');
const newDict = {};

Object.keys(dict).map((key, index) => {
  if (newDict[dict[key]] === undefined) newDict[dict[key]] = [];
  newDict[dict[key]].push(key);
  return index;
});

console.log(newDict);
