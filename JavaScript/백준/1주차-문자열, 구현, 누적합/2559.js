const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const inpu = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const line1 = inpu[0].split(' ').map(i => parseInt(i))
const array = inpu[1].split(' ').map(i => parseInt(i))

let max = Number.NEGATIVE_INFINITY;

for(let i=0; i<line1[0]-line1[1]+1; i++){
    let cash = 0;
    for (let j=i; j<i+line1[1]; j++){
        cash += array[j];
    }

    if (cash >= max){
        max = cash;
    }
}

console.log(max)