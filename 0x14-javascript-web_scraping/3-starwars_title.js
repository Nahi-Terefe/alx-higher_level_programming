#!/usr/bin/node
'use strict';
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], { json: true }, function (err, res, b) {
  if (err) console.log(err); else {
    if (res.statusCode === 200) console.log(b.title);
  }
});
