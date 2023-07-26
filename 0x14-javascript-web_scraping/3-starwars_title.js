#!/usr/bin/node
// Script to print the title of a Star Wars movie based on the given movie ID.

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
