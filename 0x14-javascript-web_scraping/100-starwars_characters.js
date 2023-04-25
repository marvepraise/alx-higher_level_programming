#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(
  `https://swapi-api.hbtn.io/api/films/${argv[0]}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(
      JSON.parse(body).characters.map((url) =>
        request.get(url, (error, response, body) => {
          if (error) {
            console.log(error);
            return;
          }
          console.log(JSON.parse(body).name);
        })
      )
    );
  }
);
