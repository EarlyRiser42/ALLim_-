function solution(elements) {
    let answer = new Set()
    let length = elements.length
    elements = elements.concat(elements)
    let j = 1
    for(let i=1; i<= length; i++){
        for(let j=0; j< length; j++){
            let cash = elements.slice(j, j+i)
            answer.add(cash.reduce((a,b)=>a+b))
        }
    }
    return answer.size;
}