const fs = require('fs');
//const inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

// DFS 함수 정의
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]
function dfs(row,col){
    board[row][col] = 0
    for (let i=0; i<4; i++){
        const nrow = row + dx[i]
        const ncol = col + dy[i]
        if(0 <= ncol && ncol < COLUMN && 0 <= nrow && nrow < ROW && board[nrow][ncol] === 1){
            dfs(nrow, ncol)
        }
    }
}

const T = Number(inpu[0])
let nextK = 0

for (let i=0; i<T; i++){
    ROW = Number(inpu[1+nextK].split(' ')[1])
    COLUMN = Number(inpu[1+nextK].split(' ')[0])
    const K = Number(inpu[1+nextK].split(' ')[2])
    let answer = 0
    // 배열 초기화
    board = new Array(ROW).fill(0)
    for (let j = 0; j < ROW; j++) {
        board[j] = new Array(COLUMN).fill(0)
    }

    for (let k=2+nextK; k< 2+nextK+K; k++){
        board[inpu[k].split(' ')[1]][inpu[k].split(' ')[0]] = 1
    }

    // DFS
    for(let row=0; row<ROW; row++){
        for (let col=0; col<COLUMN; col++){
            if (board[row][col] === 1){
                dfs(row,col)
                answer += 1
            }
        }
    }
    console.log(answer)
    nextK += K+1
}
