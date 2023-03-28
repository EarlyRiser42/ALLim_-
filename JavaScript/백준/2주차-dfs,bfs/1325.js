const fs = require('fs');
//const inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

function dfs(node){
    visited[node] = true
    for(const leaf of tree[node]){
        if (!visited[leaf]){
            cnt++
            dfs(leaf)
        }
    }
}

const [N,M] = inpu[0].split(' ').map(a => Number(a))

const tree = Array.from({ length: N + 1 }, () => []);

for (let i=1; i<= M; i++){
    const [a,b] = inpu[i].split(' ')
    tree[b].push(a)
}

let cash = []
let max = Number.NEGATIVE_INFINITY
for(let i=1; i<=N; i++){
    cnt = 0
    visited = new Array(N+1).fill(false)
    dfs(i)
    if(cnt >= max){
        max = cnt
        cash.push([i,cnt])
    }
}

let answer = []
for(const ca of cash){
    if(ca[1] === max){
        answer.push(ca[0])
    }
}

console.log(answer.join(' '))