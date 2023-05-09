function solution(n) {
    let answer = 0;
    const dp = [1, 2];

    for (let i = 0; i < n; i++) {
        dp.push((dp[i] + dp[i + 1]) % 1000000007);
    }
    return answer = dp[n - 1];
}