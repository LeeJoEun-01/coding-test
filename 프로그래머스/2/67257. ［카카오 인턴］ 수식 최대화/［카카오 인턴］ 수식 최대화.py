from copy import deepcopy
    
def solution(expression):
    arr = []
    operations = [["+","-","*"],["+","*","-"],["-","+","*"],["-","*","+"],["*","-","+"],["*","+","-"]]
    result = []
    word = ""
    
    for char in expression:
        if char == "+" or char == "-" or char == "*":
            arr.append(int(word))
            word = ""
            arr.append(char)
        else:
            word += char
    arr.append(int(word))
    
    for i in range(6):
        copy_arr = deepcopy(arr)
        
        while len(copy_arr) > 1:
            for op in operations[i]:
                while op in copy_arr:
                  for j in range (len(copy_arr)):
                      target = copy_arr[j]
                      if target == op:
                          if op == '+':
                              copy_arr[j-1] = copy_arr[j-1] + copy_arr[j+1]
                          elif op == '-':
                              copy_arr[j-1] = copy_arr[j-1] - copy_arr[j+1]
                          else:
                              copy_arr[j-1] = copy_arr[j-1] * copy_arr[j+1]
                          copy_arr = copy_arr[:j]+copy_arr[j+2:]
                          break

        if copy_arr[0] < 0:
            result.append(copy_arr[0]*-1)
        else:
            result.append(copy_arr[0])
                
    answer = max(result)
    
    return answer