const fs = require('fs');
//let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
let input = fs.readFileSync("input.txt").toString().trim().split('\r\n')

const N = Number(input[0])
const nutrition = input[1].split(' ').map(a => Number(a))
const list = []

for(let i=0; i<N; i++){
    list.push(input[i+2].split(' ').map(a=> Number(a)))
}

let visited = new Array(N).fill(false)
let cash = []
let answer = ''
let min = Number.POSITIVE_INFINITY

function backtrack(carbon, protein, fat, vitamin, cost){
    if(carbon >= nutrition[0] && protein >= nutrition[1] && fat >= nutrition[2] && vitamin >= nutrition[3]) {
        if (cost < min) {
            min = cost
            answer = [...cash]
        } else if (cost === min) {
            for(let j=0; j<cash.length; j++){
                if(cash[j] < answer[j]){
                    answer = [...cash]
                    return
                }
                else if(cash[j] > answer[j]){
                    return
                }
            }
        }
        return
    }

    for(let i=0; i<N; i++){
        if(!visited[i] && cost <= min){
            if(carbon <= nutrition[0] || protein <= nutrition[1] ||
                fat <= nutrition[2] || vitamin  <= nutrition[3]){
                visited[i] = true
                cash.push(i+1)

                backtrack(carbon + list[i][0], protein + list[i][1], fat + list[i][2], vitamin + list[i][3], cost + list[i][4])

                cash.pop()
                visited[i] = false
            }

        }
    }
}

backtrack(0,0,0,0,0)
if(answer){
    console.log(min)
    console.log(answer.join(' '))
}
else{
    console.log(-1)
}
