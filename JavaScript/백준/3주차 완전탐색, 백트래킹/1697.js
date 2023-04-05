const fs = require('fs');
//let [N, K] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(a => Number(a))
let [N, K] = fs.readFileSync("input.txt").toString().trim().split(' ').map(a => Number(a))

function BFS(x, k){
    let queue = [x]
    while(queue.length){
        let y = queue.shift()
        if(y === k){
            return array[y]
        }
        for(const move of [y-1, y+1, 2*y]){
            if(move <= 100001 && !array[move]){
                queue.push(move)
                // 걸리는 시간 체크
                array[move] = array[y]+1
            }
        }
    }
}

const MAX = 100001
array = new Array(MAX).fill(0)
const answer = BFS(N, K)
console.log(answer)
