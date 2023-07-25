#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
}

// Check if the script is run from the command line with the file path and content arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> "<string_to_write>"');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];

  writeToFile(filePath, content);
}
