const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');
const [H, W] = inpu[0].split(' ').map(a=>Number(a))

let board = new Array(H)
for (let i=0; i<H; i++){
    board[i] = inpu[i+1].split('')
}

let answer = ''

for (let i=0; i<H; i++){
    for(let j=0; j<W; j++){
        const standard = board[i].slice(0,j+1).lastIndexOf('c')
        if(standard === -1){
            answer += '-1'+' '
        }
        else{
            answer += String(j-standard)+' '
        }
    }
    answer += '\n'
}

console.log(answer)