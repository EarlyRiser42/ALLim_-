const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n').map(a=> Number(a));
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n').map(a=> Number(a));

const N = inpu[0]

for(let j=1; j<=N; j++){
    let answer = 0
    let i = 5
    while (i<= inpu[j]){
        answer += parseInt(inpu[j]/i)
        i *= 5
    }
    console.log(answer)
}



