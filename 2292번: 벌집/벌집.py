#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2292                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2292                           #+#        #+#      #+#     #
#    Solved: 2025/04/17 23:33:28 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

# N = int(sys.stdin.readline().rstrip())

# start = 2
# cnt = 1
# term = 0

# while N >= start:
#   term += 6
#   start += term
#   cnt += 1

# print(cnt)

# N = int(sys.stdin.readline().rstrip())
# inputs = [ sys.stdin.readline().rstrip() for _ in range(N)]

# KBS1_index = 0
# KBS2_index = 0

# for i in range(N):
#   input = inputs[i]

#   if input == "KBS1":
#     KBS1_index = i
#   elif input == "KBS2":
#     KBS2_index = i

# if KBS1_index > KBS2_index:
#   KBS2_index += 1

# print("1"*KBS1_index+"4"*KBS1_index+"1"*KBS2_index+"4"*(KBS2_index-1))


def solution(coin, cards):
    answer = 1
    n = len(cards)
    N = n+1
    select = set(cards[:n//3])
    stack = cards[n//3:]
    trash = set()

    for i in range(len(stack)//2):

        # 카드 2개 꺼내고
        for tmp in stack[2*i: 2*i+2]:
            # 합이 N이 되는 수가 Select에 있으면 카드 선택
            if N-tmp in select and coin >= 1:
                coin -= 1
                select.add(tmp)
            else:
                trash.add(tmp)

        # select에서 합이 N인 카드 삭제
        check1 = False
        for s in select:
            if N-s in select:
                select.remove(s)
                select.remove(N-s)
                answer += 1
                check1 = True
                break

        if check1:
            continue

        # select + trash 조합
        check2 = False
        for s in select:
            if N-s in trash and coin >= 1:
                coin -= 1
                select.remove(s)
                trash.remove(N-s)
                answer += 1
                check2 = True
                break

        if check2:
            continue

        # trash에서만 뽑아서 합 만들기
        for t in trash:
            if N-t in trash and coin >= 2:
                coin -= 2
                trash.remove(t)
                trash.remove(N-t)
                answer += 1
                break

        # 합이 되는 카드 못 만들면 종료
        else:
            return answer

    return answer


print(solution(8, [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]))
