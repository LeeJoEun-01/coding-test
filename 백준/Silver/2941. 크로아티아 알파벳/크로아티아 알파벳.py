import sys

input = list(sys.stdin.readline().rstrip())
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# ljes=njak
# li e s= nj a k

index = 0
count = 0
while index < len(input):
    # print(f"== index: {index} char:{input[index]}")
    char = input[index]

    if index >= len(input)-2:
        if index+1 <= len(input)-1:
            char += input[index+1]
            if char in alpha:
                index += 2
            else:
                index += 2
                count += 1

        count += 1
        break

    if char == 'd':
        char += input[index+1]
        if char in alpha:
            index += 2
        else:
            char += input[index+2]
            if char in alpha:
                index += 3
            else:
                index += 1
    else:
        char += input[index+1]
        if char in alpha:
            index += 2
        else:
            index += 1

    count += 1

print(count)
