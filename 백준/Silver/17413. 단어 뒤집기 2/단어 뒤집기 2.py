import sys

input = sys.stdin.readline().rstrip()
arr = list(input)
arr.append(" ")
i = 0
result = ""
word = ""
isWord = True

while i < len(arr):
    # print(f"== i: {i}-{arr[i]}| word: {word} | re: {result}")

    if arr[i] == "<":
        if isWord == True:
            re_word = word[::-1]
        result += re_word
        word = arr[i]
        isWord = False
    elif arr[i] == ">":
        word += arr[i]
        result += word
        word = ""
        isWord = True
    elif arr[i] == " ":
        if isWord == True:
            re_word = word[::-1]
            re_word += arr[i]
            result += re_word
            word = ""
        else:
            word += " "
    else:
        word += arr[i]

    i += 1

print(result)