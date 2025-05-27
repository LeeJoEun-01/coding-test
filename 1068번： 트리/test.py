import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
target = int(input())
graph = [[] for _ in range(N)]
for i in range(N) :
    temp = []   
    for l in range(N) :
        if i == nodes[l] :
            graph[i].append(l)

print(graph)
            

def backtracking(t) :
    if len(graph[t]) == 0 :
        graph[t].append(-1)
        return
    else :
        for i in range(len(graph[t])):
            backtracking(graph[t][i])
            index = graph[t].index(graph[t][i])
            graph[t][index] = -1

if nodes[target] == -1 :
    print(0)
    exit()
else :
    backtracking(target)


answer = 0
for i in range(N) :
    if len(graph[i]) == 0 :
        answer += 1
if answer == 0 :
    print(1)
else :
    print(answer)