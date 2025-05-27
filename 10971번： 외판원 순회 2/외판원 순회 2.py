#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10971                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10971                          #+#        #+#      #+#     #
#    Solved: 2025/03/14 22:21:42 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys
# input = sys.stdin.readline
# from math import inf

# N = int(input().rstrip())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*N
# ans = inf

# def dfs(v, depth, w):
#   global ans

#   if depth == N-1:
#     if arr[v][0] != 0:
#       if w+arr[v][0] < ans:
#         ans = w+arr[v][0]
#     return

#   for i in range(1,N):
#     if visited[i] == 0 and arr[v][i] != 0:
#       visited[i] = 1
#       dfs(i, depth+1, w+arr[v][i])
#       visited[i] = 0

# dfs(0,0,0)
# print(ans)

from collections import deque

def solution(land):
    answer = 0
    cnt = 0
    N = len(land[0])
    M = len(land)
    visited = [[False]*N for _ in range(M)]
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    
    print(N)
    print(M)
    
    def bfs():
        global cnt
        
        print("bfs")
        while q:
            x, y = q.popleft()
            cnt += 1
            
            for i in range(4):
                newX = x+dx[i]
                newY = y+dy[i]
                
                if 0<= newX < M and 0<= newY < N:
                    if land[newX][newY] == 1 and visited[newX][newY] == False:
                        q.append([newX, newY])
        
    for i in range(N):
        print(f"== {N}")
        visited = [[False]*N for _ in range(M)]
        cnt = 0
        for j in range(M):
            if land[j][i] == 1 and visited[j][i] == False:
                q.append([j,i])
                bfs()
                cnt += cnt
            
        if answer > cnt:
            answer = cnt
            
    return answer

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))