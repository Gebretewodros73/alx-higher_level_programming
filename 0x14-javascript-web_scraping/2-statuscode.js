#!/usr/bin/node
const https = require('https');

function displayStatusCode (url) {
  https
    .get(url, (response) => {
      const statusCode = response.statusCode;
      console.log(`code: ${statusCode}`);
    })
    .on('error', (error) => {
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
