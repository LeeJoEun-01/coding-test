# Greedy
# 1541. 잃어버린 괄호

input = input()

# 문자열 숫자와 연산자로 구분헤서 배열 만들기
input = input.replace('+', '*+*').replace('-', '*-*')
arr = input.split('*')

# print(arr)

while len(arr) > 1:
    if '+' in arr:
        for i in range(len(arr)):
            if arr[i] == '+':
                temp = int(arr[i-1]) + int(arr[i+1])
                arr[i-1] = temp
                del arr[i]
                del arr[i]
                break
    elif '-' in arr:
        for i in range(len(arr)):
            if arr[i] == '-':
                temp = int(arr[i-1]) - int(arr[i+1])
                arr[i-1] = temp
                del arr[i]
                del arr[i]
                break

print(arr[0])
