import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
result = []
ans = 0

for i in range(N):
    if arr[i] > ans+arr[i]:
        ans = arr[i]
    else:
        ans += arr[i]
    result.append(ans)
#     print(f"=== i: {i} | ans: {ans}")

# print(result)
print(max(result))