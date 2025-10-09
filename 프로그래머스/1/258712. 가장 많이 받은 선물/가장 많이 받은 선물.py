def solution(friends, gifts):
    answer = 0
    dic_f = {}
    N = len(friends)
    
    i = 0
    for name in friends:
        dic_f[name] = i
        i += 1
    
    results = [[0 for _ in range(N)] for _ in range(N)]
    for line in gifts:
        a, b = line.split(" ")
        results[dic_f[a]][dic_f[b]] += 1
    
    # 선물지수
    gifts = [0]*N
    for i in range(N):
        give, get = 0, 0
        for j in range(N):
            give += results[i][j]
        
        for j in range(N):
            get += results[j][i]
        
        gifts[i] = give-get
        
    result = [0]*N
    for i in range(N-1):
        for j in range(i+1,N):
            if results[i][j] > results[j][i]:
                result[i] += 1
            elif results[i][j] < results[j][i]:
                result[j] += 1
            else:
                if gifts[i] > gifts[j]:
                    result[i] += 1
                elif gifts[i] < gifts[j]:
                    result[j] += 1
        
    answer = max(result)
    
    return answer