import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = [input().rstrip() for _ in range(N)]
chars = []
answer = []

for i in range(N):
    word = words[i]
    candidates = []
    isFirst = True
    isDone = False
    for j in range(len(word)):
        if word[j].lower() not in chars and isFirst:
            chars.append(word[j].lower())
            tmp = words[i][0:j]+"["+word[j]+"]"+words[i][j+1:]
            answer.append(tmp)
            isDone = True
            break
        elif word[j] == " ":
            isFirst = True
        else:
            candidates.append([j, word[j]])
            isFirst = False

    if isDone == False:
        for j in range(len(candidates)):
            if candidates[j][1].lower() not in chars:
                chars.append(word[candidates[j][0]].lower())
                tmp = words[i][0:candidates[j][0]] + \
                    "["+word[candidates[j][0]]+"]" + \
                    words[i][candidates[j][0]+1:]
                answer.append(tmp)
                isDone = True
                break

    if isDone == False:
        answer.append(word)

for ans in answer:
    print(ans)