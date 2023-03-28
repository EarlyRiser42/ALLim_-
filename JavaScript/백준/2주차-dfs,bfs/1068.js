const fs = require('fs');
//let [N, ...inpu] = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
let [N, ...inpu] = fs.readFileSync("input.txt").toString().trim().split('\r\n')

const input = inpu[0].split(' ').map(a => Number(a))
const leaf = Number(inpu[1])

function dfs(node){
    visited[node] = true
    for(const leaf of tree[node]){
        if (!visited[leaf]){
            cnt++
            dfs(leaf)
        }
    }
}

function delete_node(node){
    visited[node] = true
    deleted.push(node)
    for(const leaf of tree[node]){
        if (!visited[leaf]){
            delete_node(leaf)
        }
    }
}

const tree = Array.from({ length: Number(N)}, () => [])
visited = Array.from({ length: Number(N)}, () => false)

for(let i=0; i<input.length; i++){
    if (input[i] !== -1) tree[input[i]].push(i)
}

deleted = []
delete_node(leaf)
for(let k=0; k<N; k++){
    tree[k] = tree[k].filter(a => !deleted.includes(a))
}


let answer = 0

for (let j = 0; j < N; j++) {
    visited = Array.from({ length: Number(N)}, () => false)
    cnt = 0
    dfs(j)
    if (cnt === 0 && deleted.indexOf(j) === -1) answer++
}

console.log(answer)
