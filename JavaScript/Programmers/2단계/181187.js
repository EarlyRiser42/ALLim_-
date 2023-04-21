function solution(r1, r2) {
    let [x,y] = [r2, 1]
    let [r2_sum, r1_sum] = [0,0]

    while(x){
        if(Math.sqrt(x**2+y**2) > r2){
            x--
        }
        else{
            r2_sum += x
            y++
        }
    }
    r2_sum *= 4
    r2_sum += 4*r2

    x = r1
    y= 1

    while(x){
        if(Math.sqrt(x**2+y**2) < r1){
            r1_sum += x
            y++
        }
        else{
            x--
        }
    }
    r1_sum *= 4
    r1_sum += 4*r1
    return r2_sum - r1_sum + 4;
}
