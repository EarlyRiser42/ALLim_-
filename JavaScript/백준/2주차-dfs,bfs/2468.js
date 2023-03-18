const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]
function dfs(row,col,j){
    copyboard[row][col] = 0
    for (let i=0; i<4; i++){
        const drow = row + dx[i]
        const dcol = col + dy[i]
        if (0 <= drow && drow< N && 0 <= dcol && dcol < N && copyboard[drow][dcol] !== 0){
            dfs(drow,dcol,j)
        }
    }
}

const N = Number(inpu[0])

// 2차원 배열 초기화

let board = new Array(N)
for (let i=0; i<N; i++){
    board[i] = inpu[1+i].split(' ').map(a=>Number(a))
}

let answer = 0

for (let j =0; j<=101; j++){
    let cash = 0
    copyboard = board.map(a => [...a]);
    for(let row=0; row<N; row++){
        for(let col=0; col<N; col++){
            if (copyboard[row][col] <= j){
                copyboard[row][col] = 0
            }
        }
    }

    for(let row=0; row<N; row++){
        for(let col=0; col<N; col++){
            if (copyboard[row][col] !== 0){
                cash += 1
                dfs(row,col,j)
            }
        }
    }

    if(cash > answer){
        answer = cash
    }
}

console.log(answer)