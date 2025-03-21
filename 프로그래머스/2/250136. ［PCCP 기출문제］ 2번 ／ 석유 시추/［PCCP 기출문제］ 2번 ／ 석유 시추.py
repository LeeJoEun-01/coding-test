from collections import deque
cnt = 0

def solution(land):
    global cnt
    answer = 0
    N = len(land[0])
    M = len(land)
    total = [0]*N
    group_cols = []
    visited = [[False]*N for _ in range(M)]
    
    q = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs():
        global cnt 
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                newX = x+dx[i]
                newY = y+dy[i]
                
                if 0<= newX < M and 0<= newY < N:
                    if land[newX][newY] == 1 and visited[newX][newY] == False:
                        q.append([newX,newY])
                        visited[newX][newY] = True
                        cnt += 1
                        group_cols.append(newY)
    num = 0
    for i in range(M):
        for j in range(N):
            cnt = 1
            group_cols = []
            if land[i][j] == 1 and visited[i][j] == False:
                q.append([i,j])
                group_cols.append(j)
                visited[i][j] = True
                bfs()
            
                set_cols = list(set(group_cols))
                for cols in set_cols:
                    total[cols] += cnt
                    
    return max(total)