function solution(numbers) {
    var answer = numbers.reduce((a, b) => (a + b))/numbers.length
    return answer;
}