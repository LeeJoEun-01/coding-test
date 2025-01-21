import operator

def solution(genres, plays):
    plays_dic = {}
    total_dic = {}
    for i in range(len(plays)):
        genre = genres[i]
        if genre in total_dic:
            total_dic[genre] += plays[i]
            plays_dic[genre].append([i,plays[i]])
        else:
            total_dic[genre] = plays[i]
            plays_dic[genre] = [[i,plays[i]]]
    
    sort_dic = dict(sorted(total_dic.items(), key=lambda x:-x[1]))
    
    answer = []
    for key in sort_dic:
        values = plays_dic[key]
        values.sort(key = lambda x:(-x[1],x[0]))
        
        if len(values) >= 2:
            answer.append(values[0][0])
            answer.append(values[1][0])
        else:
            answer.append(values[0][0])
        
    return answer