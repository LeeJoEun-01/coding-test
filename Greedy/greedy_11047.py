# Greedy
# 11047. 동전 0

N, K = map(int, input().split())
count = 0

arr = [int(input()) for _ in range(N)]
arr.reverse()

for i in arr:
    target = i

    # while문으로 풀었더니 시간초과 뜸... ㅜㅜ
    # while (K-target >= 0):
    #     K = K - target
    #     if K < 0:
    #         break
    #     count += 1

    if (K - target) >= 0:
        num = K//target
        K = K - target*num
        count += num

print(count)
