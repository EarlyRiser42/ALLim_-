const fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let input = fs.readFileSync('input.txt').toString().trim().split('\r\n');
const N = input.lastIndexOf('.')

for (let i=0; i< N; i++){
    let stack = []
    for (const Parenthesis of input[i]){
        if (stack[stack.length-1] === '(' && Parenthesis === ')'){
            stack.pop()
        }
        else if (stack[stack.length-1] === '[' && Parenthesis === ']'){
            stack.pop()
        }
        else if (Parenthesis === ']' || Parenthesis === ')' || Parenthesis === '(' || Parenthesis === '['){
            stack.push(Parenthesis)
        }
    }

    if (stack.length >0){
        console.log('no')
    }
    else{
        console.log('yes')
    }
}