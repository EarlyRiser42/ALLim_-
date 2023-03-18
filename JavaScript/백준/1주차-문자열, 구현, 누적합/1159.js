const input = require('fs')
    .readFileSync('dev/stdin')
    .toString()
    .trim()
    .split('\n');

let dic = {}

for (let i = 97; i <= 122; i++) {
    dic[String.fromCharCode(i)] = 0;
}

for (let j=1; j<= parseInt(input[0]); j++){
    dic[input[j][0]] += 1
}

let answer = ''
for (let k = 97; k <= 122; k++) {
    if (dic[String.fromCharCode(k)] >= 5) {
        answer += String.fromCharCode(k)
    }
}

if (answer){
    console.log(answer)
}
else{
    console.log('PREDAJA')
}