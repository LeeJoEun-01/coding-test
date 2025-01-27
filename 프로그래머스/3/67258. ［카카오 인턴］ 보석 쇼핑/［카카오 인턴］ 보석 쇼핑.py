
def solution(gems):
    num = len(set(gems))
    start = 0
    end = 0
    answer = [0,len(gems)-1]
    dic = {gems[0]:1}
    
    if num == 1:
        return [1, 1]
    
    while start < len(gems) and end < len(gems):
        if len(dic) < num:
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0)+1

        else:
            # 길이가 짧은거 갱신
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start, end]
            
            # start 이동
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

    return [answer[0]+1, answer[1]+1]