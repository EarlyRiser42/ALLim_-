const fs = require('fs');
//let inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const N = parseInt(inpu[0])
const M = parseInt(inpu[1])
const array = inpu[2].split(' ').map(a=>parseInt(a)).sort((a,b)=>{return a-b})

let answer = 0
let start = 0
let end = N-1

while (start < end) {
    if(array[start]+array[end] === M){
        start += 1
        end -= 1
        answer += 1
    }
    else if(array[start]+array[end] < M){
        start += 1
    }
    else{
        end -= 1
    }
}

console.log(answer)