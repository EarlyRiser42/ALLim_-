function solution(money) {
    var div = parseInt(money/5500)
    var mod = money%5500
    var answer = [div,mod];
    return answer;
}