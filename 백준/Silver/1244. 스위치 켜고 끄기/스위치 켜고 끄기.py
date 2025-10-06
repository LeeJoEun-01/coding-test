import sys

input = sys.stdin.readline

N = int(input().rstrip())
switches = list(map(int, input().split()))
switches.insert(0, 0)
n = int(input().rstrip())
students = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if students[i][0] == 1:
        # 남자
        for j in range(1, N+1):
            if students[i][1]*j > N:
                break
            else:
                tmp = students[i][1]*j
                switches[tmp] = 0 if switches[tmp] == 1 else 1
    else:
        # 여자
        start = students[i][1]
        end = students[i][1]

        while start > 1 and end < N and switches[start-1] == switches[end+1]:
            start -= 1
            end += 1

        # print(f"== start: {start} | end: {end}")
        for j in range(start, end+1):
            switches[j] = 0 if switches[j] == 1 else 1


switches = switches[1:]
for i in range(N):
    print(switches[i], end=" ")
    if (i+1) % 20 == 0:
        print()
