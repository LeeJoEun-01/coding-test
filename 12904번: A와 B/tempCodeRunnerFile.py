while deq:
    target = deq.popleft()

    if target.count(A) < aCounting:
        addA = target.append("A")
        deq.append(addA)
        reverseB = target[:-1].append("B")
        deq.append(reverseB)

    print(f"== target: {target} | deq: {deq}")