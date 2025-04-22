def solution(n, tops):
    answer = 0
    a = [ 0 for _ in range(n)]
    b = [ 0 for _ in range(n)]
    
    a[0] = 1
    b[0] = 3 if tops[0] == 1 else 2
    
    for k in range(1,n):
        a[k] = b[k-1] + a[k-1]
        if tops[k] == 0:
            b[k] = a[k-1] + b[k-1]*2
        else:
            b[k] = a[k-1]*2 + b[k-1]*3
        
        a[k] %= 10007
        b[k] %= 10007
    
    answer = (a[-1]+b[-1])%10007
        
    return answer