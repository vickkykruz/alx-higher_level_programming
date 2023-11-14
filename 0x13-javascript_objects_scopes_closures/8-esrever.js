#!/usr/bin/node

/* Write a function that returns the reversed version of a list: */

exports.esrever = function (list) {
  const reverseList = [];
  for (const item of list) reverseList.unshift(item);
  return reverseList;
};
