//let nums = require("fs").readFileSync("/dev/stdin").toString().trim().split("\r\n");
let nums = require("fs").readFileSync("input.txt").toString().trim().split("\r\n");
let array = Array.from({length: 101}, () => 0);

for (i=1; i<4; i++){
    for (j= nums[i].split(' ').map(i => parseInt(i))[0]; j<= nums[i].split(' ').map(i => parseInt(i))[1]; j++){
        array[j] += 1
    }
}

let k = 0 ;
let rslt = 0;
let one = 0;
let two = 0;
let three = 0;

while (k<101){
    if (array[k] === 1){
        one += 1;
        rslt += nums[0].split(' ').map(i => parseInt(i))[0];
    }
    else if(array[k] === 2){
        two += 1;
        rslt += 2*nums[0].split(' ').map(i => parseInt(i))[1];
    }
    else if(array[k] === 3){
        three += 1;
        rslt += 3*nums[0].split(' ').map(i => parseInt(i))[2];
    }
    k += 1;
}

console.log(one, two, three)
console.log(rslt)
