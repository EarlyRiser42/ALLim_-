//let input = require("fs").readFileSync("/dev/stdin").toString()
let input = require("fs").readFileSync("input.txt").toString()
let answer = '';

for(let i=0; i<input.length; i++){
    if(65<=input.charCodeAt(i) && input.charCodeAt(i)<=90){
        if(input.charCodeAt(i)+13 > 90){
            answer += String.fromCharCode(-90+input.charCodeAt(i)+13+65-1);
        }
        else{
            answer += String.fromCharCode(input.charCodeAt(i)+13);
        }
    }
    else if(97<=input.charCodeAt(i) && input.charCodeAt(i)<=122){
        if(input.charCodeAt(i)+13 > 122){
            answer += String.fromCharCode(-122+input.charCodeAt(i)+13+97-1);
        }
        else{
            answer += String.fromCharCode(input.charCodeAt(i)+13);
        }
    }
    else{
        answer += input[i]
    }
}

console.log(answer)