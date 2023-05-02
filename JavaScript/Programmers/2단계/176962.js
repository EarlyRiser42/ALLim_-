function htom(time){
    return Number(time.slice(3,5))+Number(time.slice(0,2))*60
}

function solution(plans) {
    var answer = [];
    for(plan of plans){
        plan[1] = htom(plan[1])
        plan[2] = Number(plan[2])
    }
    plans.sort((a,b)=>(a[1]-b[1]))
    let current_time = plans[0][1]
    while(plans.length){
        for(let i=0; i<plans.length; i++){
            if(i === plans.length-1){
                answer.push(plans[i][0])
                for(let j=0; j<i; j++){
                    plans[j][2] = plans[j][2] - (plans[j+1][1] - plans[j][1])
                }
                current_time = plans[i][1]+plans[i][2]
                for(let j=0; j<i; j++){
                    plans[j][1] = current_time
                }
                plans.pop()
                break
            }
            if(plans[i][1]+plans[i][2] <= plans[i+1][1]){
                answer.push(plans[i][0])
                for(let j=0; j<i; j++){
                    plans[j][2] = plans[j][2] - (plans[j+1][1] - plans[j][1])
                }
                current_time = plans[i][1]+plans[i][2]
                for(let j=0; j<i; j++){
                    plans[j][1] = current_time
                }
                plans.splice(i,1)
                break
            }
        }
    }
    return answer;
}
