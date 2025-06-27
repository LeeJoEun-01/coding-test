def solution(name, yearning, photo):
    answer = []
    dict = {}
    
    for i in range(len(name)):
        dict[name[i]] = i
        
    for line in photo:
        ans = 0
        for na in line:
            if na in dict:
                index = dict[na]
                ans += yearning[index]
        answer.append(ans)
