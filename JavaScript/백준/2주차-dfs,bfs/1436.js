const fs = require('fs');
//const inpu = Number(fs.readFileSync("/dev/stdin").toString().trim())
let inpu = Number(fs.readFileSync("input.txt").toString().trim())

let i = BigInt(666)
let j = 0
while(j < 10001){
    if(String(i).includes('666')){
        j++
    }
    if(j === inpu){
        console.log(String(i))
        break
    }
    i++
}

