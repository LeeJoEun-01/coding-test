from itertools import combinations

def check(com):
    n = len(com)
    key_combi = []
    for i in range(len(com[0])):
        tmp = []
        for j in range(n):
            tmp.append(com[j][i])

        if tmp in key_combi:
            return False
        key_combi.append(tmp)
            
    return True



def solution(relation):
    answer = 0
    result = 0
    cols_num = len(relation[0])
    cols = [[] for _ in range(cols_num)]
    for line in relation:
        for i in range(len(line)):
            cols[i].append(line[i])
    

    candidates = []
    for i in range(len(cols)):
        if len(cols[i]) != len(set(cols[i])):
            candidates.append(cols[i])
        else:
            answer += 1

    keys = []

    n = len(candidates)
    for i in range(2, n + 1):
        for idxs in combinations(range(n), i):
            
            skip = False
            cand_key = set([k for k in idxs])
            
            for key in keys:
                key = set(key)
                if key.issubset(cand_key):
                    skip = True
                    
            if skip == False:
                com = []
                for idx in idxs:
                    com.append(candidates[idx])
                
                if check(com):
                    keys.append(cand_key)
                    answer += 1
            
    
    return answer