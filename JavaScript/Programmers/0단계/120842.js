function solution(num_list, n) {
    var answer = [];
    for (i=0; i<num_list.length; i+=n){
        cash = new Array
        for(j=0; j<n; j++){
            cash.push(num_list[j+i]);
        }
        answer.push(cash);
    }
    return answer;
}