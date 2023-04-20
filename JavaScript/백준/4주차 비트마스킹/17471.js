const fs = require('fs');
//let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
let input = fs.readFileSync("input.txt").toString().trim().split('\r\n')

const N = Number(input[0])
const population = input[1].split(' ').map(a => Number(a))
const list = new Array(N)

for(let i=0; i<N; i++){
    list[i+1] = (input[i+2].split(' ').slice(1,).map(a=> Number(a)))
}

function backtrack(){
    
}