#!/usr/bin/node
// print the first argument passed to the this script

let argv = process.argv;
let firstArg = '';

argv.forEach((value, key) => {
    if (key === 2) {
        firstArg = value;        
    }
});

if (firstArg === ''){
    console.log('No argument');
}else {
    console.log(firstArg);
}
