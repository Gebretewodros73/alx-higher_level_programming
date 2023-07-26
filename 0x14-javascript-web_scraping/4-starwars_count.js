#!/usr/bin/node
const fs = require('fs');

function countMoviesWithCharacter (apiURL) {
  const characterID = 18; // Wedge Antilles character ID
  const url = `${apiURL}${characterID}/`;

  fs.get(url)
    .then((response) => {
      console.log(response.data.films.length);
    })
    .catch((error) => {
      console.error(`Error: ${error.message}`);
    });
}

// Check if the script is run from the command line with the API URL argument
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
} else {
  const apiURL = process.argv[2];
  countMoviesWithCharacter(apiURL);
}
