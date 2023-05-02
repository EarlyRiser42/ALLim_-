function solution(dirs) {
    let answer = []
    let current = [5,5]
    let cash = 0
    for(const dir of dirs){
        if(dir=== 'U' && 0<=current[0]-1 && current[0]-1 <10){
            cash = [...current]
            current[0]--
            if(!([cash, current] in answer) && !([current, cash] in answer)){
                answer.push([...cash, ...current])
            }

        }
        else if(dir === 'D' && 0<=current[0]+1 && current[0]+1 <10){
            let cash = [...current]
            current[0]++
            if(!([cash, current] in answer) && !([current, cash] in answer)){
                answer.push([...cash, ...current])
            }
        }
        else if(dir === 'R' && 0<=current[1]+1 && current[1]+1 <10){
            let cash = [...current]
            current[1]++
            if(!([cash, current] in answer) && !([current, cash] in answer)){
                answer.push([...cash, ...current])
            }
        }
        else if(dir === 'L' && 0<=current[1]-1 && current[1]-1 <10){
            let cash = [...current]
            current[1]--
            console.log([...cash, ...current])
            console.log(...answer)
            console.log(!([...cash, ...current] in answer))
            if(!([...cash, ...current] in answer) && !([...current, ...cash] in answer)){
                answer.push([...cash, ...current])
            }
        }
    }
    console.log(answer)
    return answer.length
}

solution("ULURRDLLU")