#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');
const concatenatedData = dataA + dataB;

fs.writeFileSync(fileC, concatenatedData);
