const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n").map(v=>v.split(' ').map(x=>+x));
//let input = fs.readFileSync("input.txt").toString().trim().split('\r\n');

const [N,M] = input.shift();
const home = [];
const chicken = [];
const chick_dist = [];
let answer = 2000000;


for(let i =0; i<N; i++){
    for(let j = 0; j<N; j++){
        if(input[i][j]==1){
            home.push({"hi":i,"hj":j})
            chick_dist.push([])
        }else if(input[i][j]==2){
            chicken.push({"ci":i,"cj":j})
        }
    }
}
const all_chick = chicken.length;

home.forEach((h,i)=>{
    const {hi,hj} = h;
    chicken.forEach((c,k)=>{
        const {ci,cj} = c;
        const dist = Math.abs(hi-ci)+Math.abs(hj-cj);
        chick_dist[i].push(dist)
    })
})


for(let k = 0; k<(1<<all_chick);k++){
    if(countBits(k)<=M){
        const combination = [];
        for(let l = 0; l<all_chick; l++){
            if(k&(1<<l)){
                combination.push(l);
            }
        }
        let sum = 0;
        chick_dist.forEach((v,i)=>{
            const tempdist = v;
            sum+=Math.min(...tempdist.filter((_,k)=>combination.includes(k)))
        })
        if(sum<answer) answer = sum
    }
}

console.log(answer)


function countBits(value){
    let count  = 0;
    while(value>0){
        if((value&1)==1) count++;
        value = value>>1;
    }
    return count;
}