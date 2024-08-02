N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

S = 0
arrA.sort()  # 오름차순 정렬
arrB.sort(reverse=True) # 내림차순 정렬

for i in range(N):
  S += arrA[i]*arrB[i]

print(S)