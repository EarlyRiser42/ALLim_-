function backtrack(minerals, limit, visited, cash, i){
    if(cash.length === limit){
        let sum = 0
        let i = 0
        for(let c of cash){
            if(c===0){
                let j=i+5
                while(i<j){
                    if(minerals[i]){
                        sum += cost[0][minerals[i]]
                    }
                    i++
                }
            }
            else if(c === 1){
                let j=i+5
                while(i<j){
                    if(minerals[i]){
                        sum += cost[1][minerals[i]]
                    }
                    i++
                }
            }
            else{
                let j=i+5
                while(i<j){
                    if(minerals[i]){
                        sum += cost[2][minerals[i]]
                    }
                    i++
                }
            }
        }
        if(sum < min){
            min = sum
        }
        return
    }
    for(let index=0; index<pick.length; index++){
        if(!visited[index]){
            visited[index] = true
            cash.push(pick[index])
            backtrack(minerals, limit, visited ,cash, i+1)
            visited[index] = false
            cash.shift()
        }
    }
}

function solution(picks, minerals) {
    cost = {0:{'diamond':1, 'iron':1, 'stone':1},
        1:{'diamond':5, 'iron':1, 'stone':1},
        2:{'diamond':25, 'iron':5, 'stone':1}
    }
    min = Number.POSITIVE_INFINITY
    pick = []
    for([index, element] of picks.entries()){
        for(let i=0; i<element; i++){
            pick.push(index)
        }
    }
    let visited = new Array(pick.length).fill(false)
    let limit = Math.ceil(minerals.length/5)
    const max = pick.length
    if(max<limit){
        limit = max
    }
    backtrack(minerals , limit, visited, [], 0)
    return min
}

solution(	[1, 1, 0], ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"])