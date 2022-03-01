#!/usr/bin/node
// Handle arguments

let argvEelement = process.argv.length;
if (argvEelement <= 2) {
    console.log('No argument')
}else if(argvEelement === 3) {
    console.log('Argument found')
}else if(argvEelement > 3) {
    console.log('Arguments found')
}
