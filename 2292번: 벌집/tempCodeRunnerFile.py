def solution(coin, cards):
	answer = 0
	n = len(cards)
	N = n+1
	select = cards[:n//3]
	trash = []
	isDone = False
	
	for i in range(n//3,n,2):
		if isDone:
			break

		answer += 1
		for j in (i,i+1):
			tmp = cards[j]

			if N-tmp in select:
				if coin >= 1:
					coin -= 1
					select.append(tmp)
			else:
				trash.append(tmp)
    
		for j in range(round(len(select)/2)):
				tmp = select[j]
				
				if N-tmp in select:
					select.remove(tmp)
					select.remove(N-tmp)
					isDone = True
					print(f"= delete: {tmp}, {N-tmp}")

		if isDone == False:
				for t in range(round(len(trash)/2)):
						tmp = trash[t]

						if N-tmp in trash:
							if coin >= 2:
								coin -= 2
								select.append(tmp)
								select.append(N-tmp)
								trash.remove(tmp)
								trash.remove(N-tmp)
		else:
			isDone = False
	
	return answer