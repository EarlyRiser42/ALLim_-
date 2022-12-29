function solution(my_string, letter) {
    var answer = '';
    for (s of my_string){
        if (s != letter){
            answer += s
        }
    }
    return answer;
}