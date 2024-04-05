def makeChange(coins, total):
    tp = [float('inf')] * (total + 1)
    tp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            tp[i] = min(tp[i], tp[i - coin] + 1)

    if tp[total] == float('inf'):
        return -1
    else:
        return tp[total]

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
