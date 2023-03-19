const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const NM = inpu[0].split(' ').map(a=>Number(a))
const N = NM[0]
const M = NM[1]
const J = Number(inpu[2])
const apple = inpu.slice(2,inpu.length).map(a=>a-1)

let answer = 0
let bucket = [...Array(M).keys()]
for(let j=0; j<J; j++){
    for(let i=0;i<N;i++){
        if(apple[j] in bucket){
            answer += 1
            break
        }
        bucket.map(a=>a+1)
    }
}

console.log(answer)