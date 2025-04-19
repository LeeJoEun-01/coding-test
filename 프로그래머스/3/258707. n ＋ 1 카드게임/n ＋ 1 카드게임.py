def solution(coin, cards):
    answer = 1
    n = len(cards)
    N = n + 1
    hand = set(cards[:n // 3])
    stack = cards[n // 3:]
    temp = set()

    for i in range(len(stack) // 2):
        # 2개 카드 꺼내기
        for x in stack[2 * i:2 * i + 2]:
            if N - x in hand and coin >= 1:
                coin -= 1
                hand.add(x)
            else:
                temp.add(x)

        # 1단계: hand 내에서 짝 제거
        check1 = False
        for x in hand:
            if N - x in hand:
                hand.remove(x)
                hand.remove(N - x)
                answer += 1
                check1 = True
                break

        if check1:
            continue

        # 2단계: hand, temp 조합
        check2 = False
        for x in hand:
            if N - x in temp and coin >= 1:
                coin -= 1
                hand.remove(x)
                temp.remove(N - x)
                answer += 1
                check2 = True
                break

        if check2:
            continue

        # 3단계: temp 내에서 2개 코인 써서 구매
        for x in temp:
            if N - x in temp and coin >= 2:
                coin -= 2
                temp.remove(x)
                temp.remove(N - x)
                answer += 1
                break
        else:
            # 아무것도 못 했으면 종료
            return answer

    return answer