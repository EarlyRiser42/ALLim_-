const fs = require('fs');
//const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const N = Number(input[0])
let board = []
for(let i=0; i<N; i++){
    board[i] = input[i+1].split(' ').map(a => Number(a))
}

let visited = Array.from({length: N}, () => new Array(N).fill(false))
let answer = Number.POSITIVE_INFINITY

console.log(visited)
const dx = [0,0,1,-1]
const dy = [1,-1,0,0]
function BFS(x,y){
    let queue = [[x,y]]
    let cash = 0
    let cnt = 0
    visited[x][y] = true
    while(queue.length){
        let [r,c] = queue.shift()
        for(let i=0; i<4; i++){
            const nx = r + dx[i]
            const ny = c + dy[i]
            if(0<= nx && nx < N && 0<= ny && ny < N && !visited[nx][ny] && !visited[nx-1][ny] && !visited[nx+1][ny] && !visited[nx][ny-1] && !visited[nx][ny+1]){
                for(let _=0; _<4; _++){
                    const nxx = nx + dx[i]
                    const nyy = ny + dy[i]
                    visited[nxx][nyy] = true
                    cash += board[nxx][nyy]
                }
                queue.push([nx,ny])
                for(let _=0; _<4; _++){
                    const nxx = nx + dx[i]
                    const nyy = ny + dy[i]
                    visited[nxx][nyy] = false
                }
            }
        }
    }
}