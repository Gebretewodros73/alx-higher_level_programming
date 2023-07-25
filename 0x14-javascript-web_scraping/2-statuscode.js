#!/usr/bin/node
const axios = require('axios');

function displayStatusCode (url) {
  axios.get(url)
    .then((response) => {
      console.log(`code: ${response.status}`);
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
