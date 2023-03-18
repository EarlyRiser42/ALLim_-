const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const inpu = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const NM = inpu[0].split(' ').map(i => parseInt(i))

let dicbynumber = {};
let dicbyname = {};
for (let i=1; i<=NM[0]; i++){
    dicbynumber[i] = inpu[i];
    dicbyname[inpu[i]] = i
}

let answer = '';
for(let j=NM[0]+1; j<NM[0]+NM[1]+1; j++){
    if (isNaN(inpu[j])){
        answer += String(dicbyname[inpu[j]])+'\n';
    }
    else{
        answer += String(dicbynumber[inpu[j]])+'\n';
    }
}

console.log(answer)