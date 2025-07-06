line= input()
stack=[]
count = 0
for i in range(len(line)):
    if line[i] == "(":
        stack.append("(")
    else :
        if line[i-1]=="(":
            stack.pop()
            count+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.
            
        else :
            stack.pop()
            count+=1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.
print(count)