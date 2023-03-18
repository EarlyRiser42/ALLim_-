const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const NM = inpu[0].split(' ').map(a=>Number(a))
const N= Number(NM[0])
const M = Number(NM[1])

let board = []
for (let i=1; i<=N; i++){
    board.push(inpu[i].split('').map(a=>Number(a)))
}

// BFS
let queue = [[0,0,1]]
let answer = 0
const move = [[0,1], [1,0], [-1,0], [0,-1]]

while (queue.length !== 0){
    let cash = queue.shift()
    board[cash[0]][cash[1]] = 0
    for (let i=0; i<4; i++){
        const row = cash[0] + move[i][0]
        const col = cash[1] + move[i][1]
        // dx: 행, dy: 열
        if (0<= row && row < N && 0 <= col && col < M){
            if(board[row][col] === 1){
                queue.push([row,col, cash[2]+1])
                board[row][col] = 0
            }
        }
    }
    if (cash[0] === N-1 && cash[1] === M-1){
        answer = cash[2]
        break
    }
}

console.log(answer)