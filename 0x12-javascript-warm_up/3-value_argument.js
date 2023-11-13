#!/usr/bin/node
/*
 * a script that prints the first argument passed to it
 */

const argCount = process.argv.slice(2)

if (argCount[0]) {
  console.log(argCount[0]);
} else { console.log('No argument'); }
