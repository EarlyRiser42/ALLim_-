const fs = require('fs');
//const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let input = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const [N, L, R] = input[0].split(' ').map(a => Number(a))
const board = Array.from({length: N}, ()=> [])
for(let i=0; i<N; i++){
    board[i] = input[i+1].split(' ').map(a => Number(a))
}

let answer = 0

for(let k=0; k<2001; k++){
    let uni = 0
    let list = []
    visited = Array.from({length: N}, ()=> {})
    for(let _=0; _<N; _++){
        visited[_] = Array.from({length: N}, () => {}).fill(false)
    }

    for(let row=0; row<N; row++){
        for(let col=0; col<N; col++){
            const [cash, sum] = BFS(row,col)
            if(cash.length>1){
                list.push([cash, Math.floor(sum/cash.length)])
                uni++
            }
        }
    }

    for(const li of list){
        for(const l of li[0]){
            board[l[0]][l[1]] = li[1]
        }
    }


    if(uni>0){
        answer++
    }
    else{
        break
    }
}

console.log(answer)

function BFS(r,c){
    const dx = [0, 0, 1, -1]
    const dy = [1, -1, 0, 0]

    let sum = board[r][c]
    let union = [[r,c]]
    let queue = [[r,c]]
    visited[r][c] = true

    while(queue.length){
        const cash = queue.shift()
        for(let i =0; i<4; i++){
            const nrow = cash[0] + dx[i]
            const ncol = cash[1] + dy[i]
            if(0<= nrow && nrow < N && 0 <= ncol && ncol < N && !visited[nrow][ncol] && L <= Math.abs(board[nrow][ncol]-board[cash[0]][cash[1]]) &&
                Math.abs(board[nrow][ncol]-board[cash[0]][cash[1]]) <= R){
                sum += board[nrow][ncol]
                union.push([nrow,ncol])
                queue.push([nrow,ncol])
                visited[nrow][ncol] = true
            }
        }
    }
    return [union, sum]
}
