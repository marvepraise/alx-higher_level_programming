#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  // console.log(JSON.parse(body));
  const result = JSON.parse(body);
  const answer = {};
  result.forEach((user) => {
    if (user.completed) {
      answer[user.userId]
        ? (answer[user.userId] += 1)
        : (answer[user.userId] = 1);
    }
  });
  console.log(answer);
});
