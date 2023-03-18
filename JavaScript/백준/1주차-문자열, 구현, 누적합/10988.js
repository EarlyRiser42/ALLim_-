//let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(i => parseInt(i));
let input = require("fs").readFileSync("input.txt").toString().trim();
let reverse = input.split('').reverse().join('')

if(input === reverse){
    console.log(1)
}
else{
    console.log(0)
}