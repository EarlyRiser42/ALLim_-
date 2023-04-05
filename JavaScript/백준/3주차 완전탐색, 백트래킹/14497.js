const fs = require('fs');
//const inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
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