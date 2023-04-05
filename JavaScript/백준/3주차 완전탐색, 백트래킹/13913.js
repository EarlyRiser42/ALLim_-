const fs = require('fs');
//let [N, K] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(a => Number(a))
let [N, K] = fs.readFileSync("input.txt").toString().trim().split(' ').map(a => Number(a))

function BFS(x, k){
    let queue = [x]
    let array = new Array(MAX).fill(0)
    let path = new Array(MAX).fill(0)
    if(x === k){
        return [0, x]
    }
    else{
        while(queue.length){
            let y = queue.shift()
            if(y === k){
                const min = array[y]
                let backtrack = String(k)
                let start = y
                while(start !== x){
                    backtrack = String(path[start]) + ' '+backtrack
                    start = path[start]
                }
                return [min, backtrack]
            }
            for(const move of [y-1, y+1, 2*y]){
                if(move <= 100001 && !array[move]){
                    queue.push(move)
                    // 걸리는 시간 체크
                    array[move] = array[y]+1
                    path[move] = y
                }
            }
        }
    }
}

const MAX = 100001
const [min, track] = BFS(N, K)
console.log(min)
console.log(track)
