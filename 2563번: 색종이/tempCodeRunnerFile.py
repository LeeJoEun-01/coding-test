import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
duplication = 0

for i in range(N):
    # 겹치는 부분 좌표 구하기
    x, y = arr[i]
    for j in range(i+1, N):
        xx, yy = arr[j]
        if x+10 > xx and y+10 > yy:
            if yy < y:
                a = [xx, y]
                b = [xx, yy+10]
                c = [x+10, y]
            else:
                a = [xx, yy]
                b = [xx, y+10]
                c = [x+10, yy]
            duplication += (c[0]-a[0])*(b[1]-a[1])
            break
        else:
            break

print(100*N-duplication)