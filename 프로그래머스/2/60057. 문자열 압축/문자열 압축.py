def solution(s):
    num = len(s)
    result = []
    
    if num == 1:
        return 1
    if num == 2:
        return 2
    
    for i in range(1,num+1):
        line = ""
        count = 1
        temp = s[:i]
        for j in range (i, num+i, i):
            if temp == s[j:i+j]:
                count += 1
            else:
                if count != 1:
                    line = line+f"{count}"+temp
                else:
                    line = line + temp
                
                temp = s[j:j+i]
                count = 1
                
        result.append([line, len(line)])
        
    result.sort(key = lambda x: x[1])
    return result[0][1]