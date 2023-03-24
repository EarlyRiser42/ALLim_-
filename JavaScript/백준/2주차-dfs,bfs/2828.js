const fs = require('fs');
const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');

const [N,M] = inpu[0].split(' ').map(a=>Number(a))
const J = Number(inpu[1])
const apples = inpu.slice(2,inpu.length).map(a=> Number(a))

let answer = 0
let start = 1
let end = M

for(let apple of apples){
    if (end < apple){
        answer += apple - end
        end = apple
        start = apple - (M - 1)
    }

    else if (start > apple){
        answer += start - apple
        start = apple
        end = apple + (M - 1)
    }
}

console.log(answer)