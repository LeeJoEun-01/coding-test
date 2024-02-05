# Implementation
# 1158. 요세푸스 문제

from collections import deque

n, k = map(int, input().split())

# 숫자 배열 만들기
arr = deque()
for i in range(1, n+1):
    arr.append(i)

# k번째 사람 제거하기
result = []

while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
