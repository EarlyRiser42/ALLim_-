const fs = require('fs');
//const inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]
function dfs(row,col){
    size += 1
    board[row][col] = 1
    for (let i=0; i<4; i++){
        const drow = row + dx[i]
        const dcol = col + dy[i]
        if (0 <= drow && drow< M && 0 <= dcol && dcol < N && board[drow][dcol] === 0){
            dfs(drow,dcol)
        }
    }


}

const MNK = inpu[0].split(' ').map(a=>Number(a))
M = Number(MNK[0])
N = Number(MNK[1])
const K = Number(MNK[2])

board = new Array(M)
for (let _=0; _<M; _++){
    board[_] = new Array(N).fill(0)
}

for (let i=1; i<=K; i++){
    const input = inpu[i].split(' ').map(a=>Number(a))
    const row_start = M-input[3]
    const row_end = M-input[1]-1
    const col_start = input[0]
    const col_end = input[2]-1
    for(let row=row_start; row<= row_end; row++){
        for(let col=col_start; col<= col_end; col++){
            board[row][col] = 1
        }
    }
}
let answer = 0
let answer_2 = []
for (let row=0; row<M; row++){
    for(let col=0; col<N; col++){
        if(board[row][col] === 0){
            size = 0
            dfs(row,col)
            answer_2.push(size)
            answer += 1
        }
    }
}

console.log(answer)
console.log(...answer_2.sort((a,b)=>a-b))