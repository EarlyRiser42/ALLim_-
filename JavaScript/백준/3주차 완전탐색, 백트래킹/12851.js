const fs = require('fs');
//let [N, K] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(a => Number(a))
let [N, K] = fs.readFileSync("input.txt").toString().trim().split(' ').map(a => Number(a))

function BFS(x, k){
    // 걸리는 시간
    let array = new Array(MAX).fill(0)
    // 경우의 수
    let array2 = new Array(MAX).fill(0)
    let queue = [x]
    array2[x] = 1
    if(x === k){
        return [0, 1]
    }
    while(queue.length){
        let y = queue.shift()
        for(const move of [y-1, y+1, 2*y]){
            if(move <= 100001){
                if(array[move] === 0){
                    queue.push(move)
                    // 걸리는 시간 체크
                    array[move] = array[y]+1
                    // 경우의 수
                    array2[move] += array2[y]
                }
                else if(array[move] === array[y] +1){
                    array2[move] += array2[y]
                }
            }
        }
    }
    return [array[k], array2[k]]
}

const MAX = 100001
const [a, b] = BFS(N, K)
console.log(a)
console.log(b)
