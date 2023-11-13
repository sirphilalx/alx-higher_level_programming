#!/usr/bin/node

/*
 * a process that outputs based on the number of arguments
 */

const argCount = process.argv.length - 2;

if (argCount === 2){
    console.log('Arguments found');
}else if(argCount === 1){
    console.log('Argument found);
}else{
    console.log('No argument found');
}
