#!/usr/bin/node
const fs = require('fs');

function displayStatusCode (url) {
  fs.get(url)
    .then((response) => {
      const statusCode = response.status;
      console.log(`code: ${statusCode}`);
    })
    .catch((error) => {
      console.error(`Error: ${error.message}`);
    });
}

// Check if the script is run from the command line with the URL argument
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
} else {
  const url = process.argv[2];
  displayStatusCode(url);
}
