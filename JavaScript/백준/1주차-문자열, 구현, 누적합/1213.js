const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim();
let inpu = fs.readFileSync("input.txt").toString().trim();
inpu = inpu.split('').sort()
let dic = {}
for (let i=0; i<inpu.length; i++){
    dic[inpu[i]] = 0
}
for (let i=0; i<inpu.length; i++){
    dic[inpu[i]] +=1
}

let start = ''
let end = ''
for(let [i, element] of Object.values(dic).entries()) {
    // 짝수
    if(element % 2 === 0){
        const count = element/2
        start += Object.keys(dic)[i].repeat(count)
    }
    // 홀수
    else{
        const count = (element-1)/2
        start += Object.keys(dic)[i].repeat(count)
        end += Object.keys(dic)[i]
    }
}

const cash = start
const reverse_cash = cash.split('').reverse().join('')
let answer = ''
if (end){
    answer = cash + end + reverse_cash
}
else{
    answer = cash + end + reverse_cash
}

if (answer.length % 2 === 0){
    if (answer.slice(0,answer.length/2) === answer.slice(answer.length/2,answer.length).split('').reverse().join('')){
        console.log(answer)
    }
    else{
        console.log("I'm Sorry Hansoo")
    }
}
else{
    if (answer.slice(0,answer.length/2) === answer.slice((answer.length/2)+1,answer.length).split('').reverse().join('')){
        console.log(answer)
    }
    else{
        console.log("I'm Sorry Hansoo")
    }
}