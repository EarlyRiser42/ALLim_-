function solution(m, n, board) {
    let answer = 0;
    let cash = 1
    while(cash){
        cash = 0
        let deleted = []
        for(let r=0; r<m-1; r++){
            for(let c=0; c< n-1; c++){
                if(board[r][c] !== '0' && board[r][c] === board[r][c+1] && board[r][c+1] === board[r+1][c+1] && board[r+1][c+1] === board[r+1][c]){
                    for(const [x,y] of [[r,c], [r+1, c], [r,c+1], [r+1, c+1]]){
                        if(!(deleted.some(item => item.join() === [x, y].join()))){
                            deleted.push([x,y])
                        }
                    }
                }
            }
        }
        cash = deleted.length
        answer += cash

        // 일치하는 문자열 지우기
        for(const [r,c] of deleted){
            board[r] = board[r].slice(0,c)+'0'+board[r].slice(c+1,n)
        }

        // 아래로 내리기
        for(let c=0; c<n; c++){
            let cash = ''
            for(let r=m-1; r>=0; r--){
                cash += board[r][c]
            }
            let zero = 0
            for(let i=0; i<m; i++){
                if(cash[i] === '0'){
                    zero++
                }
            }
            cash = cash.replace(/0/g, "")+'0'.repeat(zero)
            for(let r=0; r<m; r++){
                board[r] = board[r].slice(0,c) + cash[m-r-1] + board[r].slice(c+1,n)
            }
        }
    }
    return answer;
}
