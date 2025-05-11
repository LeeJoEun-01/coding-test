import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
re_arr = arr[::-1]

increase = [1]*N
decrease = [1]*N

for i in range(N):
    for j in range(i):

        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

        if re_arr[i] > re_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

decrease.reverse()

ans = 0
for i in range(N):
    s = increase[i]+decrease[i]-1
    if ans < s:
        ans = s

print(ans)