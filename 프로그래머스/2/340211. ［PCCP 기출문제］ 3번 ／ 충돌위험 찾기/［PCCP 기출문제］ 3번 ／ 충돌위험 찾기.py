def findRoutes(points):
    results = []
    r = points[0][0]
    c = points[0][1]
    
    for i in range(1,len(points)):
        if i == 1:
            line = [[r,c]]
        else:
            line = []

        endR = points[i][0]
        endC = points[i][1]
        
        while r != endR or c != endC:
            if r > endR:
                r -= 1
            elif r < endR:
                r += 1
            else:
                if c > endC:
                    c -= 1
                elif c < endC:
                    c += 1
                else:
                    break
            
            line.append([r,c])            
        results += line
    
    return results
    

def solution(points, routes):
    answer = 0
    result = []
    lens = []
    
    for line in routes:
        arr = []
        for v in line:
            arr.append(points[v-1])
        
        tmp = findRoutes(arr)
        result.append(tmp)
        lens.append(len(tmp))

    # print(f"=== result: {result}")

    for j in range(max(lens)):
        target = []
        notTarget = []
        for i in range(len(routes)):
            if lens[i] > j:
                # print(f"🌟===: i: {i} | j:{j}  = {result[i][j]}")
                if result[i][j] in target:
                    # print(f"===: i: {i} | j:{j}  = {result[i][j]}")
                    target.remove(result[i][j])
                    if result[i][j] not in notTarget:
                        answer += 1
                    notTarget.append(result[i][j]) 
                target.append(result[i][j])
    
    return answer