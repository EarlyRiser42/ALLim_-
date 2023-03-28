const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = Number(inpu[0])

for (let i=1; i<=N; i++){
    let stack = []
    for (const Parenthesis of inpu[i]){
        if (stack[stack.length-1] === '(' && Parenthesis === ')'){
            stack.pop()
        }
        else{
            stack.push(Parenthesis)
        }
    }
    if (stack.length >0){
        console.log('NO')
    }
    else{
        console.log('YES')
    }
}