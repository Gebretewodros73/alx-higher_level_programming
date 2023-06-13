#!/usr/bin/node
const { list } = require('./data/100-data');

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
