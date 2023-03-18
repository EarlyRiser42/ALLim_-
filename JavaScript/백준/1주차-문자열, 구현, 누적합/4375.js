const fs = require('fs');
//let inpu = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

for (let i=0; i<inpu.length; i++){
    for(let j=1; j<100000; j++){
        if(BigInt('1'.repeat(j)) % BigInt(inpu[i]) === BigInt(0)){
            console.log(j)
            break
        }
    }
}
