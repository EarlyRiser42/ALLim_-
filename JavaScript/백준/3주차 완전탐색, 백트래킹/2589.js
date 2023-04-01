const fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let input = fs.readFileSync("input.txt").toString().trim().split('\r\n');
const [ROW, COLUMN] = input[0].split(' ').map(a => Number(a))


// BFS 함수 정의
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]
function bfs(r, c){
    let max2 = 0
    let queue = [[r,c,0]]
    visited[r][c]= true
    while(queue.length){
        const cash =  queue.shift()
        if(cash[2] >= max2){
            max2 = cash[2]
        }
        for (let i=0; i<4; i++){
            const nrow = cash[0] + dx[i]
            const ncol = cash[1] + dy[i]
            if(0 <= nrow && nrow < ROW && 0 <= ncol && ncol < COLUMN && board[nrow][ncol] === 'L' && !visited[nrow][ncol]) {
                // BFS이므로 한번 이동할때마다 이동거리가 1증가하는것이 아닌 이전 이동거리에서 +1 해야함
                queue.push([nrow, ncol, cash[2]+1])
                // visited 체크를 여기서 해야함
                visited[nrow][ncol] = true
            }
        }
    }
    return max2
}

const board = Array.from({ length: ROW}, () => []);
for(let i=0; i<ROW; i++){
    board[i] = input[i+1].split('')
}

let answer = Number.NEGATIVE_INFINITY

for (let row = 0; row < ROW; row++) {
    let min = 0
    for (let col = 0; col < COLUMN; col++) {
        if (board[row][col] === 'L') {
            visited = Array.from({length: ROW}, () => [])
            for (let _ = 0; _ < ROW; _++) {
                visited[_] = Array.from({length: COLUMN}, () => []).fill(false)
            }
            min = bfs(row, col)
            if (min >= answer) {
                answer = min
            }
        }
    }

}

console.log(answer)