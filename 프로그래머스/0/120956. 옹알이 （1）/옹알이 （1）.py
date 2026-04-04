def solution(babbling):
    answer = 0
    target = ["aya","ye","woo","ma"]
    
    for word in babbling:
        print(f"= word: {word}")
        idx = 0
        for t in target:
            tmp = word.find(t)
            if tmp != -1:
                word = word.replace(t," ")
                # print(f"== word: {word}")
                
        word = word.strip()
        if len(word) == 0:
            answer += 1
    
    return answer