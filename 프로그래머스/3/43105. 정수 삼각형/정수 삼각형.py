def solution(triangle):
    len_tri = len(triangle)
    dp = triangle
    for n in range(1,len_tri):
        length = len(triangle[n])
        for i in range(length):
            if i == 0:
                dp[n][i] += dp[n-1][0]
            elif i == length-1:
                dp[n][i] += dp[n-1][i-1]
            else:
                dp[n][i] += max(dp[n-1][i-1], dp[n-1][i])
                
    answer = max(dp[len_tri-1])
    return answer