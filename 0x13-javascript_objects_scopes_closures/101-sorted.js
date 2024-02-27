#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const key in dict) {
  const occurrences = dict[key].toString();
  if (!(occurrences in sortedDict)) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(key);
}

console.log(sortedDict);
