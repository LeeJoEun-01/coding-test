N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# x[1] => 끝나는 시간이 빠를 수록
# x[0] => 끝나는 시간이 같다면 시작하는 시간이 빠를수록
arr.sort(key=lambda x: (x[1], x[0]))
count = 0
endTime = 0

for i in arr:
    startTime = i[0]
    if startTime >= endTime:
        endTime = i[1]
        count += 1

print(count)
