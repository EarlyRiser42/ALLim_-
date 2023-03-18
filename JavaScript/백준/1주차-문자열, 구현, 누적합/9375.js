const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split("\n");
const inpu = fs.readFileSync("input.txt").toString().trim().split("\r\n");

const N = parseInt(inpu[0]);
const cloth = [];
const M = [0];

for(let i=1; i<inpu.length; i++){
    if(!isNaN(inpu[i])) {
        M.push(parseInt(inpu[i]));
    }
    else{
        cloth.push(inpu[i]);
    }
}
console.log(cloth)
console.log(M)
for(let i=0; i<N; i++){
    let dic = {};
    const start = M.slice(0,i+1).reduce((a,b)=> a+b);
    for(let j= start; j< start+M[i+1]; j++){
        dic[cloth[j].split(' ')[1]] = 0;
    }

    for(let k= start; k< start+M[i+1]; k++){
        dic[cloth[k].split(' ')[1]] += 1;
    }

    // 정답 출력 파트
    if (Object.keys(dic).length === 1){
        console.log(Object.values(dic)[0]);
    }
    else{
        const values = Object.values(dic)
        let answer = 1;
        for (value of values){
            answer *= (value+1);
        }
        console.log(answer-1);
    }

}

