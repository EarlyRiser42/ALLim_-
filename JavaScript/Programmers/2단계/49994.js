function solution(dirs) {
    let answer = []
    let current = [5,5]
    let cash = 0
    for(const dir of dirs){
        if(dir=== 'U' && 0<=current[0]-1 && current[0]-1 <11){
            let cash = [...current]
            current[0]--
            if(!(answer.some(item => item.join() === [cash, current].join())) && !(answer.some(item => item.join() === [current, cash].join()))){
                answer.push([cash, [...current]])
            }

        }
        else if(dir === 'D' && 0<=current[0]+1 && current[0]+1 <11){
            let cash = [...current]
            current[0]++
            if(!(answer.some(item => item.join() === [cash, current].join())) && !(answer.some(item => item.join() === [current, cash].join()))){
                answer.push([cash, [...current]])
            }
        }
        else if(dir === 'R' && 0<=current[1]+1 && current[1]+1 <11){
            let cash = [...current]
            current[1]++
            if(!(answer.some(item => item.join() === [cash, current].join())) && !(answer.some(item => item.join() === [current, cash].join()))){
                answer.push([cash, [...current]])
            }
        }
        else if(dir === 'L' && 0<=current[1]-1 && current[1]-1 <11){
            let cash = [...current]
            current[1]--
            if(!(answer.some(item => item.join() === [cash, current].join())) && !(answer.some(item => item.join() === [current, cash].join()))){
                answer.push([cash, [...current]])
            }
        }
    }
    return answer.length
}
