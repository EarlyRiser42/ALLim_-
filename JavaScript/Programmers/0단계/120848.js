function solution(n) {
    var dp = new Array(10);
    dp[0] = 1;
    for (i=1; i<dp.length; i++){
        dp[i] = dp[i-1]*(i+1)
    }
    for(j=dp.length; j>=0; j--){
        if (dp[j] <= n) {
            return j+1;
        }
    }
}