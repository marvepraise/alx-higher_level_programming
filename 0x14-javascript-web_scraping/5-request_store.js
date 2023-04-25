#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  // console.log(body);
  fs.writeFile(argv[1], body, function (error) {
    if (error) console.log(error);
  });
});
