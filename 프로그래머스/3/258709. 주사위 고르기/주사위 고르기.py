import itertools
import bisect

def solution(dice):
    answer = []
    len_dice = len(dice)
    candidates = list(itertools.combinations(range(len_dice), len_dice//2))
    max_cnt = 0
    
    # 주사위 선정
    for candi in candidates:
        A = list(candi)
        B = [b for b in range(len_dice) if b not in candi]
        
        # 주사위로 나올 수 있는 값 정리
        A_dice_list = [dice[i] for i in A]
        A_sums = [sum(combination) for combination in itertools.product(*A_dice_list)]

        B_dice_list = [dice[i] for i in B]
        B_sums = [sum(combination) for combination in itertools.product(*B_dice_list)]

        cnt = 0
        B_sums.sort()
        for a in A_sums:
            cnt += bisect.bisect_left(B_sums,a)

        if max_cnt < cnt:
            max_cnt = cnt
            answer = [a+1 for a in A]
            
    return answer