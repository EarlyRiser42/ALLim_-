const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const N = Number(inpu[0])
let answer = []

for (let i=1; i<=N; i++) {
    let cash = ''
    for(let j of inpu[i]){
        if (!isNaN(j)){
            cash += j
        }
        else if(isNaN(j)){
            if (cash.length > 0){
                answer.push(BigInt(cash))
            }
            cash = ''
        }
    }
    if (cash.length > 0){
        answer.push(BigInt(cash))
    }
}

answer.sort((a, b) => (a < b) ? -1 : ((a > b) ? 1 : 0))
console.log(answer.join('\n').trim())