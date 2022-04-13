#!/usr/bin/node
'use strict';
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/:id' + process.argv[2], { json: true }, function (e, r, b) {
  if (e) console.log(e); else {
    if (r.statusCode === 200) console.log(b.title);
  }
});
