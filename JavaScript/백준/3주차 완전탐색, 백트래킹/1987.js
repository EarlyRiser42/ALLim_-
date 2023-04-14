const fs = require('fs');
//let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
let input = fs.readFileSync("input.txt").toString().trim().split('\r\n')

const [R, C] = input[0].split(' ').map(a=> Number(a))
let board = []
for(let i=0; i<R; i++){
    board[i] = input[i+1].split('')
}

let visited = new Array(26).fill(0)
visited[board[0][0].charCodeAt(0)-65] = 1
const dx = [0,0,1,-1]
const dy = [1,-1,0,0]

let answer = 0

function DFS(r,c,cnt){
    answer = Math.max(answer, cnt)
    for(let i=0; i<4; i++){
        const nx = r + dx[i]
        const ny = c + dy[i]
        if(0<=nx && nx < R && 0<= ny && ny< C && !(visited[board[nx][ny].charCodeAt(0)-65])){
            visited[board[nx][ny].charCodeAt(0)-65] = 1
            DFS(nx,ny,cnt+1)
            visited[board[nx][ny].charCodeAt(0)-65] = 0
        }
    }
}

DFS(0,0,1)
console.log(answer)