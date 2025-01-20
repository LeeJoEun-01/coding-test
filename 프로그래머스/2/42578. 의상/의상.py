def solution(clothes):
    cloth_dic = {}
    for i in range(len(clothes)):
        category = clothes[i][1]
        if category in cloth_dic:
            cloth_dic[category] += 1
        else:
            cloth_dic[category] = 1
    
    answer = 1
    for i in cloth_dic.values():
        answer *= i+1
        
        
    return answer-1