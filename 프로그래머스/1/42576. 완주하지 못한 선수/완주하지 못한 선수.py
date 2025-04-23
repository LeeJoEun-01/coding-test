def solution(participant, completion):    
    answer = ''
    com_dic = {}
    
    for c in completion:
        com_dic.setdefault(c, 0)
        com_dic[c] += 1
    
    for p in participant:
        com_dic.setdefault(p, 0)
        com_dic[p] -= 1
        # print(f"=== dic: {com_dic}")
        if com_dic[p] == -1:
            answer = p
            break

    return answer