function solution(want, number, discount) {
    var answer = 0
    let remain = 0
    let judge = {}

    for(const [i, w] of want.entries()){
        judge[w] = number[i]
    }

    for(let i=0; i<=discount.length-10; i++){
        let dic = {}
        let cash = 0
        for(const w of want){
            dic[w] = 1
        }
        for(let j=i; j<i+10; j++){
            if(dic[discount[j]]){
                dic[discount[j]]++
            }
        }

        for(w of want){
            if(dic[w] > judge[w]){
                cash++
            }
        }
        if(cash === want.length){
            answer++
        }
    }
    return answer
}