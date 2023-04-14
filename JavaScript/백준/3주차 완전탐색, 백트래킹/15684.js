const fs = require('fs');
//const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const [N,M,H] = input[0].split(' ').map(a => Number(a))

let board = Array.from({length:H}, () => new Array(N*2-1).fill(0))

// 사다리 초기화
for(let i=0; i<H; i ++){
    for(let j=0; j<N*2-1; j+=2){
        board[i][j] = 1
    }
}

for(let i=0; i<M; i++){
    const [x,y] = input[i+1].split(' ').map(a => Number(a))
    board[x][y] = 1
}

const dx = [0,0,1,-1]
const dy = [1,-1,0,0]

let answer = 0

function DFS(r,c, visited){
    if(r === H-1){
        console.log('return', r, c)
        return c
    }
    for(let i=0; i<4; i++){
        const nx = r + dx[i]
        const ny = c + dy[i]
        if(0 <=nx && nx < H && 0 <= ny && ny< N*2-1 && board[nx][ny] === 1 && !visited[nx][ny]){
            visited[nx][ny] = true
            DFS(nx,ny,visited)
            visited[nx][ny] = false
        }
    }
}


let cnt = 0
for(let i=0; i<N*2-1; i+=2){
    let visit = Array.from({length: H}, () => new Array(N*2-1).fill(false))
    console.log(i)
    let arrive = DFS(0,i, visit)
    console.log(arrive)
    if(arrive === i){
        cnt++
    }
}
if(cnt === H){
    console.log(answer)
}