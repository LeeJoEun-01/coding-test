import sys
input = sys.stdin.readline

arr = list(input().rstrip())
lenA = arr.count('a')
# print(f"== lenA: {lenA}")

results = []
for i in range(len(arr)):
    tmp = []
    if i <= len(arr)-lenA:
        tmp = arr[i:i+lenA]
    else:
        tmp = arr[i:]+arr[:(lenA-(len(arr)-i))]

    # print(f"== i: {i}, temp: {tmp}")
    results.append(tmp.count('b'))

print(min(results))