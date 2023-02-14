def distributeCandies(candyType):
    eatly = len(candyType) // 2
    eating = []
    for i in candyType:
        if i not in eating:
            eating.append(i)
        if len(eating) == eatly:
            break
    return len(eating)
