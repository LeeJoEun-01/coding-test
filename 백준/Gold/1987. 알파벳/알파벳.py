import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

ans = set(arr[0][0])
maxN = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def backTraking(x, y, n):
    global maxN

    if n > maxN:
        maxN = n

    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]

        if 0 <= newX < R and 0 <= newY < C:
            if arr[newX][newY] not in ans:
                # print(
                #     f"=== ans: {ans} | arr[{newX}][{newY}]: {arr[newX][newY]} | count: {n+1}]")
                ans.add(arr[newX][newY])
                backTraking(newX, newY, n+1)
                ans.remove(arr[newX][newY])


backTraking(0, 0, 1)
print(maxN)