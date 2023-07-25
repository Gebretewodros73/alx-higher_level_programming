#!/usr/bin/node
const fs = require('fs');

function readFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
      console.error(error);
    } else {
      console.log(data);
    }
  });
}

// Check if the script is run from the command line with the file path argument
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file_path>');
} else {
  const filePath = process.argv[2];
  readFileContent(filePath);
}

