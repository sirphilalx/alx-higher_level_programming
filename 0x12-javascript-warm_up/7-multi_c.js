#!/usr/bin/node

/*
 * A script that prints x times “C is fun”
 */

const count = parseInt(process.argv.slice(2));

if (count && Number.isInteger(count)) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
