const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const inpu = fs.readFileSync("input.txt").toString().trim().split("\r\n");
const N = Number(inpu[0])

let answer = 0
for (let i =1; i<=N; i++){
    let queue = [inpu[i][0]];
    for (const input of inpu[i].slice(1,)){
        if(input === queue[queue.length-1]){
            queue.pop()
        }
        else{
            queue.push(input)
        }
    }
    if (queue.length === 0){
        answer += 1
    }
}

console.log(answer)