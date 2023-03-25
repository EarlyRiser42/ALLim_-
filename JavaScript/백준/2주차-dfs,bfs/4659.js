const fs = require('fs');
//const inpu = fs.readFileSync("./dev/stdin").toString().trim().split('\n');
let inpu = fs.readFileSync("input.txt").toString().trim().split('\r\n');

for (let input of inpu.slice(0,inpu.length-1)){
    let cash = ''
    let [cnt, m, j, print] = [0, 0, 0, 0]
    for (let i of input){
        if (cash !== 'e' && cash !== 'o'){
            if (i === cash){
                console.log('<'+input+'> is not acceptable.')
                print = 1
                break
            }
        }
        switch (i){
            case 'a': case'e': case'i': case'o': case'u':
                cnt++
                m++
                j = 0
                break
            default:
                j++
                m = 0
                break
        }
        cash = i
        if(m >= 3 || j >= 3){
            print = 1
            console.log('<'+input+'> is not acceptable.')
            break
        }
    }
    if (print ===0 && cnt > 0){

        console.log('<'+input+'> is acceptable.')
    }
    else if(print ===0 && cnt === 0){
        console.log('<'+input+'> is not acceptable.')
    }
}