const fs = require('fs');
//const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const [R,C,K] = input[0].split(' ').map(a => Number(a))

let board = Array.from({length: R}, () => [])
for(let i=0; i<R; i++){
    board[i] = input[i+1].split('')
}
let visited = Array.from({length:R}, () => new Array(C).fill(false))

const dx = [0,0,1,-1]
const dy = [1,-1,0,0]

let answer = 0

function DFS(r,c,cnt){
    if(r === 0 && c === C-1 && cnt === K){
        answer++
        return
    }
    for(let i=0; i<4; i++){
        const nx = r + dx[i]
        const ny = c + dy[i]
        if(0 <=nx && nx < R && 0 <= ny && ny< C && board[nx][ny] !== 'T' && !visited[nx][ny]){
            visited[nx][ny] = true
            DFS(nx,ny,cnt+1)
            visited[nx][ny] = false
        }
    }
}

visited[R-1][0] = true
DFS(R-1,0,1)
console.log(answer)