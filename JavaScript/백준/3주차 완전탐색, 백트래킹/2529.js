const fs = require('fs');
//const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const k = Number(input[0])
const inequality = input[1].split(' ')
let answer = []

function calculate(a,b,operation) {
    if (operation === '<') {
        return (a < b)
    } else {
        return (a > b)
    }
}

function backtrack(index, ans){
    if(index === k+1){
        answer.push(ans)
        return
    }
    for(let j=0; j<10; j++){
        if(!visited[j]){
            if(index === 0 || calculate(ans[index-1], j, inequality[index-1])){
                visited[j] = true
                backtrack(index+1, ans+String(j))
                visited[j] = false
            }
        }
    }
}

visited = new Array(10).fill(false)
backtrack(0, '')
answer.sort((a,b) => (a-b))
console.log(answer[answer.length-1])
console.log(answer[0])