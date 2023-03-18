//let nums = require("fs").readFileSync("/dev/stdin").toString().trim();
let nums = require("fs").readFileSync("input.txt").toString().trim();

let dic = {}

for (let i = 97; i <= 122; i++) {
    dic[String.fromCharCode(i)] = 0;
}

for (num of nums){
    dic[num] += 1;
}

console.log(Object.values(dic).join(' '));

